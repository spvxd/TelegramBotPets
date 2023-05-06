from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

load_button = KeyboardButton('/upload')
delete_button = KeyboardButton('/Удалить')


buttons_admin = ReplyKeyboardMarkup(resize_keyboard=True).add(load_button).add(delete_button)