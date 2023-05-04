from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import os
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

token_path = open('token.txt')
token = token_path.read()
bot = Bot(token=token)
dp = Dispatcher(bot=bot, storage=storage)
