# Copyright (C) 2018 - 2020 MrYacha. All rights reserved. Source code available under the AGPL.
# Copyright (C) 2019 Aiogram
#
# This file is part of SophieBot.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys

import redis as redis_lib

from sophie_bot import log
from sophie_bot.config import CONFIG

# Init Redis
redis = redis_lib.StrictRedis(
    host=CONFIG.redis_host,
    port=CONFIG.redis_port,
    db=CONFIG.redis_db_fsm,
    decode_responses=True,
    max_connections=25
)

bredis = redis_lib.StrictRedis(
    host=CONFIG.redis_host,
    port=CONFIG.redis_port,
    db=CONFIG.redis_db_fsm,
    max_connections=25
)

try:
    redis.ping()
except redis_lib.ConnectionError as err:
    sys.exit(log.critical("Can't connect to RedisDB! Exiting... Exception: " + err))
