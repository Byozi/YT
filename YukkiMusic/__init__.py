#
# Copyright (C) 2021-2022 by Byozi@Github, < https://github.com/Byozi >.
#
# This file is part of < https://github.com/Byozi/YT > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/Byozi/YT/blob/master/LICENSE >
#
# All rights reserved.

from YukkiMusic.core.bot import YukkiBot
from YukkiMusic.core.dir import dirr
from YukkiMusic.core.git import git
from YukkiMusic.core.userbot import Userbot
from YukkiMusic.misc import dbb, heroku, sudo

from .logging import LOGGER

# Directories
dirr()

# Check Git Updates
git()

# Initialize Memory DB
dbb()

# Heroku APP
heroku()

# Load Sudo Users from DB
sudo()

# Bot Client
app = YukkiBot()

# Assistant Client
userbot = Userbot()

from .platforms import *

YouTube = YouTubeAPI()
Carbon = CarbonAPI()
Spotify = SpotifyAPI()
Apple = AppleAPI()
Resso = RessoAPI()
SoundCloud = SoundAPI()
Telegram = TeleAPI()
