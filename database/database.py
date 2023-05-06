import sqlite3

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
