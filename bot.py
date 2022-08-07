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

@bot.on_message(filters.command('RIP') & filters.private)
async def start(bot, message):
    await message.reply(
        f"**{message.chat.first_name}!**\n"
        "**Sorry To Say This You Dont Have Any Subscription 😞\n Buy Subscription From @CR_0O0...**")

@bot.on_message(filters.command('Myplan') & filters.private)
async def start(bot, message):
    await message.reply(
        f"**{message.chat.first_name}!**\n"
        "**Sorry To Say This You Dont Have Any Subscription 😞\n Buy Subscription From @CR_0O0...**")

@bot.on_message(filters.command('rip') & filters.private)
async def start(bot, message):
    await message.reply(
        f"**{message.chat.first_name}!**\n"
        "**To Know About Plans Kindly Contact @CR_0O0... ☺️**")


Bot.run()
