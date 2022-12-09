from Nidhi import Nidhi, BOT_USERNAME
from Config import Config
from telethon import events, Button

PM_START_TEXT = """
ʜᴇʏ! {} 🥀
─────────────────────────
• **ɪ'ᴍ ᴀ ꜱɪᴍᴘʟᴇ ᴛᴇʟᴇɢʀᴀᴍ ᴍᴜꜱɪᴄ ʙᴏᴛ**.
"""

@Nidhi.on(events.NewMessage(pattern="^[?!/]start$"))
async def start(event):
    if Config.MANAGEMENT_MODE == "ENABLE":
        return
    if event.is_private:
       await event.client.send_file(event.chat_id,
             Config.START_IMG,
             caption=PM_START_TEXT.format(event.sender.first_name), 
             buttons=[
        [Button.url(" ᴀᴅᴅ ᴍᴇ", f"https://t.me/{BOT_USERNAME}?startgroup=true")],
        [Button.url("🥀ꜱᴜᴘᴘᴏʀᴛ", f"https://t.me/{Config.SUPPORT}"), Button.url("🍂 ᴜᴘᴅᴀᴛᴇꜱ", f"https://t.me/{Config.CHANNEL}")],
        [Button.inline("✨ ᴄᴏᴍᴍᴀɴᴅꜱ", data="help"), Button.url("🎓 ᴅᴇᴠᴇʟᴏᴘᴇʀ", url="https://t.me/Simple_Munda")]])
       return

    if event.is_group:
       await event.reply("**ʜᴇʏ! ɪ'ᴍ ᴀʟɪᴠᴇ 🌹**")
       return



@Nidhi.on(events.callbackquery.CallbackQuery(data="start"))
async def _(event):
    if Config.MANAGEMENT_MODE == "ENABLE":
        return
    if event.is_private:
       await event.edit(PM_START_TEXT.format(event.sender.first_name), buttons=[
        [Button.url("ᴀᴅᴅ ᴍᴇ", f"https://t.me/{BOT_USERNAME}?startgroup=true")],
        [Button.url("🥀 ꜱᴜᴘᴘᴏʀᴛ", f"https://t.me/{Config.SUPPORT}"), Button.url("🍂 ᴜᴘᴅᴀᴛᴇꜱ", f"https://t.me/{Config.CHANNEL}")],
        [Button.inline("✨ ᴄᴏᴍᴍᴀɴᴅꜱ", data="help"), Button.url("🎓 ᴅᴇᴠᴇʟᴏᴘᴇʀ", url="https://t.me/Simple_Munda")]])
       return
