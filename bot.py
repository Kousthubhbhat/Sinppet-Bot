from pyrogram import Client, filters
from config import *
import os

START_MESSAGE = os.environ.get("START_MESSAGE")

Bot = Client(
    "sample_bot",
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH
)

@Bot.on_message(filters.command("start") & filters.private)
async def start(bot: Client, cmd):
    return await cmd.reply_text(START_MESSAGE)
