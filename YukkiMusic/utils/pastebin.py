#
# Copyright (C) 2021-2022 by Byozi@Github, < https://github.com/Byozi >.
#
# This file is part of < https://github.com/Byozi/YT > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/Byozi/YT/blob/master/LICENSE >
#
# All rights reserved.

import aiohttp

BASE = "https://batbin.me/"


async def post(url: str, *args, **kwargs):
    async with aiohttp.ClientSession() as session:
        async with session.post(url, *args, **kwargs) as resp:
            try:
                data = await resp.json()
            except Exception:
                data = await resp.text()
        return data


async def Yukkibin(text):
    resp = await post(f"{BASE}api/v2/paste", data=text)
    if not resp["success"]:
        return
    link = BASE + resp["message"]
    return link
