# Copyright (C) 2021-2022 by Byozi@Github, < https://github.com/Byozi >.
#
# This file is part of < https://github.com/Byozi/YT > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/Byozi/YT/blob/master/LICENSE >
#
# All rights reserved.

import sys

from pyrogram import Client
from pyrogram.types import BotCommand

import config

from ..logging import LOGGER


class YukkiBot(Client):
    def __init__(self):
        LOGGER(__name__).info("Bot Göreve Çağırılıyor..")
        super().__init__(
            "YukkiMusicBot",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
        )

    async def start(self):
        await super().start()
        get_me = await self.get_me()
        self.username = get_me.username
        self.id = get_me.id  # Değişiklik burada
        try:
            await self.send_message(config.LOG_GROUP_ID, "Bot Görevini Yapmak İçin Hazır!")
        except:
            LOGGER(__name__).error("Bot log grubuna erişemedi. Botunuzu log kanalınıza eklediğinizden ve yönetici olarak atadığınızdan emin olun!")
            sys.exit()
        if config.SET_CMDS:
            try:
                await self.set_bot_commands([
                    BotCommand("ping", "Botun canlı veya ölü olup olmadığını kontrol edin"),
                    # Diğer komutlar buraya eklenebilir
                ])
            except:
                pass
        else:
            pass
        a = await self.get_chat_member(config.LOG_GROUP_ID, self.id)
        if a.status != "administrator":
            LOGGER(__name__).error("Lütfen Bot'u Log Group'ta Yönetici olarak tanıtın")
            sys.exit()
        if get_me.last_name:
            self.name = get_me.first_name + " " + get_me.last_name
        else:
            self.name = get_me.first_name
        LOGGER(__name__).info(f"MusicBot Started as {self.name}")
