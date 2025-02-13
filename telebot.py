import logging
from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
import os

load_dotenv()
TELLEGRAM_BOT_TOKEN = os.getenv("TELLEGRAM_BOT_TOKEN")

logging.basicConfig(level=logging.INFO)


bot=Bot(token=TELLEGRAM_BOT_TOKEN)
dp=Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def command_start_handler(message: types.Message):
    """
    This handler receives messages with '/start' or '/help' command
    """
    await message.reply("Hi\nIam Echo Bot\nPowered by aiogram.")

    if __name__ =="__main__":
        executor.start_polling(dp, skip_updates=True)