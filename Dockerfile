FROM python:3.11-slim as builder

ENV PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1

RUN apt update
RUN apt install build-essential gcc -y
RUN pip install poetry wheel
RUN python -m venv /venv

COPY pyproject.toml poetry.lock ./

RUN poetry export -f requirements.txt -E fast --without-hashes | /venv/bin/pip install -r /dev/stdin

COPY sophie_bot sophie_bot
RUN poetry build && /venv/bin/pip install dist/*.whl

FROM python:3.11-slim as final

ENV PYTHONFAULTHANDLER=1 \
    PYTHONHASHSEED=random \
    PYTHONUNBUFFERED=1

# RUN apk add --no-cache libffi libpq

COPY --from=builder /venv /venv
COPY sophie_bot /sophie_bot

WORKDIR /

CMD ["/venv/bin/python", "-m", "sophie_bot"]
