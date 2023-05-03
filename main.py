from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import sqlite3
import os

token_path = open('token.txt')
token = token_path.read()
bot = Bot(token=token)
dp = Dispatcher(bot=bot)
con = sqlite3.connect('pets.db')
cursor = con.cursor()


def db_manipulation():
    cursor.execute("""CREATE TABLE IF NOT EXISTS pets (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, age INTEGER)""")

    cursor.execute("""INSERT INTO pets (name, age) VALUES ('Sanya', '20')""")
    con.commit()

    # cursor.execute("""DROP TABLE pets""")


async def on_startup(_):
    print('Бот вышел в онлайн')


@dp.message_handler(commands=['start'])
async def process_start_command(msg: types.Message):
    await bot.send_message(msg.from_user.id,
                           'Привет!\nЭтот телеграм-бот предназначен для того, чтобы помочь владельцам пропавших'
                           'домашних животных находить их быстрее. Бот хранит базу данных о пропавших животных,'
                           'которая постоянно '
                           'пополняется людьми.')


@dp.message_handler(commands=['help'])
async def process_help_command(msg: types.Message):
    await bot.send_message(msg.from_user.id, "Чтобы посмотреть список команд нажми /list")


@dp.message_handler(commands=['list'])
async def process_show_list(msg: types.Message):
    await bot.send_message(msg.from_user.id, "/add\n/show\n/feedback")


@dp.message_handler(commands=['add'])
async def process_add_new(msg: types.Message):
    await bot.send_message(msg.from_user.id, "Форма добавления новых животных")


@dp.message_handler(commands=['show'])
async def process_show_pets(msg: types.Message):
    await bot.send_message(msg.from_user.id, "Список животных в базе")


@dp.message_handler(commands=['feedback'])
async def process_feedback(msg: types.Message):
    await bot.send_message(msg.from_user.id, "Обратная связь")


@dp.message_handler()
async def process_generator(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
