from aiogram import types, Dispatcher
from bot import dp, bot


# @dp.message_handler()
async def process_generator(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)


def handeler_other(dp: Dispatcher):
    dp.register_message_handler(process_generator)