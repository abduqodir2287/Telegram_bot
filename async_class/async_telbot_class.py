# This bot_class is not yet ready

import aiosqlite

class Itpark_bot_helperDB:
    def __init__(self, dbname='tech.db'):
        self.dbname = dbname
        self.tabname = ''
        self.conn = aiosqlite.connect(dbname)

    async def create_table(self, tabname='custom'):
        self.tabname = tabname
        sql = f"""
            CREATE TABLE IF NOT EXISTS {tabname}(
                "id"  INTEGER PRIMARY KEY AUTOINCREMENT,
                "fullname" TEXT, 
                "phoneNumber" TEXT,
                "course"  TEXT, 
                "passport" TEXT
                );"""
        await self.conn.execute(sql)
        await self.conn.commit()

    async def add_item(self, fullname, phoneNumber, course, passport):

        sql = f"""INSERT INTO "{self.tabname}" (fullname, phoneNumber, course, passport)
            VALUES (?, ?, ?, ?);"""
        data = (fullname, phoneNumber, course, passport)
        await self.conn.execute(sql, data)
        await self.conn.commit()


    async def delete_item(self, id):
        sql = f"""DELETE FROM {self.tabname} where id=={id};"""
        await self.conn.execute(sql)
        await self.conn.commit()

    async def select_item(self):
        sql = f"""SELECT * FROM {self.tabname};"""
        return self.conn.execute(sql).fetchall()

    async def update_item(self, id, fullname, phoneNumber, course, passport):
        sql = f"""UPDATE {self.tabname} SET 
                fullname={fullname},
                phoneNumber={phoneNumber}, 
                course={course}, 
                passport={passport} 
                WHERE id={id};"""

        await self.conn.execute(sql)
        await self.conn.commit()

