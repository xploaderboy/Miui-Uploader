import time
import asyncio
from datetime import datetime
from pyrogram import Client, filters

@Client.on_message(filters.regex("magnet"))
async def command(client, message):
    await message.reply_text("Bla Bla Bla")
