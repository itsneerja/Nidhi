import os
from telethon import Button, events
from Nidhi import *

IMG = os.environ.get(
    "PING_PIC", "https://te.legra.ph/file/3eae3d0694b9a6e0af9f3.jpg"
)
ms = 501.455

ALIVE = os.environ.get(
    "ALIVE", "[ɴᴇᴇʀᴀᴊ](https://t.me/itsneerja)"
)

CAPTION = f"**ᴘ ᴏ ɴ ɢ !**\n\n   » {ms}\n   » ᴏᴡɴᴇʀ ~ {ALIVE}"


@Nidhi.on(events.NewMessage(pattern="^/ping"))
async def _(event):
    bsdk = [[
             Button.url("sᴜᴘᴘᴏʀᴛ", url="https://t.me/DevilsHeavenMF"),
                       ]]
    await Nidhi.send_file(event.chat_id, IMG, caption=CAPTION, buttons=bsdk)
