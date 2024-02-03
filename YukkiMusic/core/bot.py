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

    async def on_started(self, _):
        get_me = await self.get_me()
        self.username = get_me.username
        self.id = get_me.id  # Değişiklik burada
        try:
            await self.send_message(config.LOG_GROUP_ID, "Bot Görevini Yapmak İçin Hazır!")
        except Exception as e:
            LOGGER(__name__).error(f"Bot log grubuna erişemedi. Hata: {e}")
            sys.exit()

        if config.SET_CMDS:
            try:
                await self.set_my_commands([
                    BotCommand("ping", "Botun canlı veya ölü olup olmadığını kontrol edin"),
                    # Diğer komutlar buraya eklenebilir
                ])
            except Exception as e:
                LOGGER(__name__).error(f"Komutları ayarlarken bir hata oluştu. Hata: {e}")
        
        a = await self.get_chat_member(config.LOG_GROUP_ID, self.id)
        if a.status != "administrator":
            LOGGER(__name__).error("Lütfen Bot'u Log Group'ta Yönetici olarak tanıtın")
            sys.exit()
        
        if get_me.last_name:
            self.name = get_me.first_name + " " + get_me.last_name
        else:
            self.name = get_me.first_name
        LOGGER(__name__).info(f"MusicBot Started as {self.name}")
