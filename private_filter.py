import os
import time
import pyrogram
from pyrogram import Client, filters

if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config
    
@pyrogram.Client.on_message(pyrogram.filters.text & (filters.private))
async def private(client, message):
    await message.reply_text("Nothing Here")
