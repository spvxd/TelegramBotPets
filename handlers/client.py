from aiogram import types, Dispatcher
from bot import bot, dp
from buttons import button_client


# @dp.message_handler(commands=['start'])
async def process_start_command(msg: types.Message):
    await bot.send_message(msg.from_user.id,
                           'Привет!\nЭтот телеграм-бот предназначен для того, чтобы помочь владельцам пропавших'
                           'домашних животных находить их быстрее. Бот хранит базу данных о пропавших животных,'
                           'которая постоянно '
                           'пополняется людьми.', reply_markup=button_client)


# @dp.message_handler(commands=['help'])
async def process_help_command(msg: types.Message):
    await bot.send_message(msg.from_user.id, "Чтобы посмотреть список команд нажми /list")


# @dp.message_handler(commands=['list'])
async def process_show_list(msg: types.Message):
    await bot.send_message(msg.from_user.id, "/add\n/show\n/feedback")


# @dp.message_handler(commands=['add'])
async def process_add_new(msg: types.Message):
    await bot.send_message(msg.from_user.id, "Форма добавления новых животных")


# @dp.message_handler(commands=['show'])
async def process_show_pets(msg: types.Message):
    await bot.send_message(msg.from_user.id, "Список животных в базе")


# @dp.message_handler(commands=['feedback'])
async def process_feedback(msg: types.Message):
    await bot.send_message(msg.from_user.id, "Обратная связь")


def handlers_client(dp : Dispatcher):
    dp.register_message_handler(process_start_command, commands=['start'])
    dp.register_message_handler(process_help_command, commands=['help'])
    dp.register_message_handler(process_show_list, commands=['list'])
    dp.register_message_handler(process_add_new, commands=['add'])
    dp.register_message_handler(process_show_pets, commands=['show'])
    dp.register_message_handler(process_feedback, commands=['feedback'])
