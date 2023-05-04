from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('/show')
b2 = KeyboardButton('/add')
b3 = KeyboardButton('/feedback')

button_client = ReplyKeyboardMarkup(resize_keyboard=True)

button_client.add(b3).add(b2).insert(b1)

