import time
import asyncio
from datetime import datetime
from pyrogram import Client, filters

@Client.on_message(filters.regex("/upload@xploaderzxbot magnet"))
async def command(client, message):
    await message.reply_text("For Magnet File Leeching \nUse Our Jarvis Uploader")
