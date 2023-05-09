from bot import dp
from aiogram.utils import executor
from handlers import client, admin, other
from database import database
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

async def on_startup(_):
    print('Бот вышел в онлайн')
    database.db_manipulation()

client.handlers_client(dp)
admin.register_handlers_admin(dp)
other.handler_other(dp)

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
