from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import os


token_path = open('token.txt')
token = token_path.read()
bot = Bot(token=token)
dp = Dispatcher(bot=bot)