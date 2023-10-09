#
# Copyright (C) 2021-2022 by Byozi@Github, < https://github.com/Byozi >.
#
# This file is part of < https://github.com/Byozi/YT > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/Byozi/YT/blob/master/LICENSE >
#
# All rights reserved.

from config import LOG, LOG_GROUP_ID
from YukkiMusic import app
from YukkiMusic.utils.database import is_on_off


async def play_logs(message, streamtype):
    if await is_on_off(LOG):
        if message.chat.username:
            chatusername = f"@{message.chat.username}"
        else:
            chatusername = "Private Group"
        logger_text = f"""
**BİRİERİ BİR ŞARKI AÇTI SANIRIM İŞTE AŞAĞIDA BİLGİSİ VAR**

**AÇILAN GRUP:** {message.chat.title} [`{message.chat.id}`]
**AÇAN KİŞİ:** {message.from_user.mention}
**AÇAN KİŞİNİN KULLANICI ADI:** @{message.from_user.username}
**AÇAN KİŞİNİN ID:** `{message.from_user.id}`
**AÇILAN GRUP LINKI:** {chatusername}

**KULLANDIGI KOMUT:** {message.text}

**StreamType:** {streamtype}"""
        if message.chat.id != LOG_GROUP_ID:
            try:
                await app.send_message(
                    LOG_GROUP_ID,
                    f"{logger_text}",
                    disable_web_page_preview=True,
                )
            except:
                pass
        return
