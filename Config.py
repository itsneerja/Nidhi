import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "10399315"))
    API_HASH = os.environ.get("API_HASH", "0ca343b34d6fb43d210b03eb0fb9b973")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5594418789:AAGoCZss-x5Dn2M0k35gUmUEyknltqi3mkY")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOKgBu5dvN9b59YpNiW8EhvAnGcnNG869i7tZzR4l0HLM3zeU5lWYcX8uPPthkG9hGL0cE45eSNr64-9KehFT_jEm6UrIZJ2-2XMnbUEVAW_PduMh3iV3AkyodGt8vfaKOPkJ-BGKUyvclwlcCFk5fpWGg1qo-MHXm4TAQeqpfOE72IWlXxF3t5GGfgtAFVwsFw_Dk24ug8uaz9fxu78n53dFcvG7cr1lmC4--yJy-YrVsCUmmno_p-5wgl5uSlDMmKy91h88k6VZW-LGBrI16G5SeJgGbSWHBcGtVszbmTpqRgHnVWshr0FhzOKTgdivBUnNFNX3qu-M-M9hIhb1zDG0uyM=")
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "NidhiMissBot")
    SUPPORT = os.environ.get("SUPPORT", "DevilsHeavenMF")
    CHANNEL = os.environ.get("CHANNEL", "TheFallenAssociation")
    START_IMG = os.environ.get("START_IMG", "https://te.legra.ph/file/3eae3d0694b9a6e0af9f3.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://te.legra.ph/file/3eae3d0694b9a6e0af9f3.jpg")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5122374270")) # required
