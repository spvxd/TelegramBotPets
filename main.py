from bot import dp
from aiogram.utils import executor
import sqlite3
from handlers import client, admin, other
con = sqlite3.connect('pets.db')
cursor = con.cursor()


def db_manipulation():
    cursor.execute("""CREATE TABLE IF NOT EXISTS pets (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, age INTEGER)""")

    cursor.execute("""INSERT INTO pets (name, age) VALUES ('Sanya', '20')""")
    con.commit()

    # cursor.execute("""DROP TABLE pets""")


async def on_startup(_):
    print('Бот вышел в онлайн')

client.handlers_client(dp)
other.handeler_other(dp)
if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
