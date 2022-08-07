from pyrogram import Client, filters
from config import *


START_MESSAGE = "Start Command"

Bot = Client(
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH
)

@Bot.on_message(filters.command("start") & filters.private)
async def start(bot: Client, cmd):
    return await cmd.reply_text(START_MESSAGE)

Bot.run()