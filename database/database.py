import sqlite3
from bot import bot, dp
def db_manipulation():
    global con, cursor
    con = sqlite3.connect("database.db")
    cursor = con.cursor()
    if con:
        print("База данных работает")
    con.execute("""CREATE TABLE IF NOT EXISTS telegram (
                img TEXT,
                name TEXT PRIMARY KEY,
                description TEXT,
                contact TEXT)
                """)
    con.commit()


async def database_command(state):
    async with state.proxy() as data:
        cursor.execute("""INSERT INTO telegram VALUES (?, ?, ?, ?)""", tuple(data.values()))
        con.commit()


async def database_read(msg):
    for ret in cursor.execute("""SELECT * FROM telegram""").fetchall():
        await bot.send_photo(msg.from_user.id, ret[0], f'Имя:{ret[1]}\nОписание:{ret[2]}\nКонтакты:{ret[-1]}')


async def database_read_all():
    return cursor.execute("""SELECT * FROM telegram""").fetchall()


async def database_delete(data):
    cursor.execute("""DELETE FROM telegram WHERE name ==?""", (data,))
    con.commit()