from ClassyMusic.core.bot import ISTKHAR
from ClassyMusic.core.dir import dirr
from ClassyMusic.core.git import git
from ClassyMusic.core.userbot import Userbot
from ClassyMusic.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = ISTKHAR()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
