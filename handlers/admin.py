from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from bot import bot, dp

class FSMAdmin(StatesGroup):
    photo = State()
    name = State()
    description = State()
    phone = State()



