from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('/show')
b2 = KeyboardButton('/add')
b3 = KeyboardButton('/feedback')

button_client = ReplyKeyboardMarkup()

button_client.add(b1).add(b2).add(b3)

