from dotenv import load_dotenv
import os
from aiogram import Bot, Dispatcher, Executor, types
from echo_bot import TELLEGRAM_BOT_TOKEN
import openai
import sys


class Reference:

    def__init__(self) - > None:
        self.reference = ""
    

reference = Reference()
model_name = "gpt-3.5-turbo"    


bot = Bot(token=TELLEGRAM_BOT_TOKEN)
dispatcher = Dispatcher(bot)


@dispatcher.message_handler(commands=['start'])
async def welcome(message: types.Message):

    """
    This handler receives messages with '/start' or '/help' command
    """
    await message.reply("Hi\nIam Telebot\nHow can I help you?")

    if __name__ =="__main__":
        executor.start_polling(dispatcher, skip_updates=True)