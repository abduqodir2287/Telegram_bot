# This bot_class is not yet ready

import aiosqlite

class helperDB:
    def __init__(self, dbname='tech.db'):
        self.dbname = dbname
        self.tabname = ''
        self.conn = await aiosqlite.connect(self.dbname)

    async def setup(self, tabname='custom'):
            """
            create table for database
            :param tabname: base name
            :return: default table name id, username
            """
            self.tabname = tabname
            sql = f"""
                CREATE TABLE IF NOT EXISTS {tabname}(
                      "id"  INTEGER PRIMARY KEY AUTOINCREMENT,
                      "userID" INTEGER,
                      "username"  TEXT
                    );"""

            await self.conn.execute(sql)

    async def add_item(self, userID: str, username: str):

        sql = f"""INSERT INTO "{self.tabname}" (userID, username)
            VALUES (?, ?);"""
        data = (userID, username)
        await self.conn.execute(sql, data)
        await self.conn.commit()


    async def delete_item(self, id):
        sql = f"""DELETE FROM {self.tabname} where id=={id};"""
        await self.conn.execute(sql)
        await self.conn.commit()

    async def select_item(self):
        sql = f"""SELECT * FROM {self.tabname};"""
        return self.conn.execute(sql).fetchall()

    async def update_item(self, id, username):
        sql = f"""UPDATE {self.tabname} SET 
                username={username}, 
                WHERE id={id};"""

        await self.conn.execute(sql)
        await self.conn.commit()

    async def log_out(self):
        await self.conn.close()
