# Copyright (C) 2018 - 2020 MrYacha. All rights reserved. Source code available under the AGPL.
# Copyright (C) 2019 Aiogram
# Copyright (C) 2017 - 2020 Telethon
from telethon import TelegramClient

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


from sophie_bot.config import CONFIG

tbot = TelegramClient(CONFIG.token.split(':')[0], CONFIG.app_id, CONFIG.app_hash)


async def start_telethon():
    await tbot._start(
        phone=None,
        password=None,
        bot_token=CONFIG.token,
        force_sms=False,
        code_callback=None,
        first_name='New user',
        last_name='',
        max_attempts=3
    )