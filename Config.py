import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", ""))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    STRING_SESSION = os.environ.get("STRING_SESSION", "")
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "NidhiMusicBot")
    SUPPORT = os.environ.get("SUPPORT", "DevilsHeavenMF")
    CHANNEL = os.environ.get("CHANNEL", "TheFallenAssociation")
    START_IMG = os.environ.get("START_IMG", "https://te.legra.ph/file/3eae3d0694b9a6e0af9f3.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://te.legra.ph/file/3eae3d0694b9a6e0af9f3.jpg")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "")) # required
