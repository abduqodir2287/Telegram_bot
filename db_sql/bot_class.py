import sqlite3

class Helperbotdb():
    def __init__(self, dbname="tech.db"):
        self.dbname = dbname
        self.tabname = ""
        self.conn = sqlite3.connect(self.dbname)

    def create_table(self, tabname:str="custom"):
        sql = f"""CREATE TABLE IF NOT EXISTS {tabname}(
            "id" INTEGER PRIMARY KEY AUTOINCREMENT,
            "info" TEXT
            );
            """
        self.tabname = tabname
        self.conn.execute(sql)
        self.conn.commit()


    def add_item(self, info:str):
        sql = f"""INSERT INTO {self.tabname}(
            info)
            VALUES(?);
            """
        data = (info)
        self.conn.execute(sql, data)
        self.conn.commit()

    # def login(self):
    #     usname = input("Enter your username>>")
    #     password = input("Enter your password>>")
    #
    #     sql = f"""SELECT * FROM {self.tabname};
    #                 """
    #     data = self.conn.execute(sql).fetchall()




    def delete_item(self, id:int):
        sql = f"""DELETE FROM {self.tabname} 
            WHERE id=={id};
            """
        self.conn.execute(sql)
        self.conn.commit()


    def select_item(self):
        sql = f"""SELECT * FROM {self.tabname};
            """
        return self.conn.execute(sql).fetchall()


    # def update_item(self, id:int, username:str,
        #             email:str, password:str):
        # sql = f"""UPDATE {self.tabname}
        #     SET username=?,
        #     email=?,
        #     password=?
        #     WHERE id=={id};
        #     """
        # data = (username, email, password)
        #
        # self.conn.execute(sql, data)
        # self.conn.commit()

