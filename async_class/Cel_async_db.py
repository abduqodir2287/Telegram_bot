# This bot is not yet ready

import aiosqlite

base = await aiosqlite.connect("Celebrites.db")
table_name = ''
async def create_table(tab_name="Users"):
    global table_name
    sql = f"""
        CREATE TABLE IF NOT EXISTS {tab_name}(
              "id"  INTEGER PRIMARY KEY AUTOINCREMENT,
              "userID" INTEGER,
              "username"  TEXT
            );"""
    await base.execute(sql)
    await base.commit()
    table_name = table_name

async def add_item(userID: str, username: str):
    sql = f"""INSERT INTO {table_name}(userID, username)
            VALUES(?, ?);"""
    data = (userID, username)
    await base.execute(sql, data)
    await base.commit()

async def select_item():
    sql = f"""SELECT * FROM {table_name};"""
    data = await base.execute(sql)
    return data.fetchall()

async def log_out():
    await base.close()

