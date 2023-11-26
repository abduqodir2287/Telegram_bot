from aiogram import *

from logging import *

from Tel_bot_lessons.config import exampe_bot_token

from datetime import *

import sqlite3


bot = Bot(token=exampe_bot_token)
basicConfig(level=INFO)
dp = Dispatcher(bot)

base = sqlite3.connect("Bot.db")
base.commit()
cur = base.cursor()
cur.execute(f"""CREATE TABLE IF NOT EXISTS Malumotlar(
            "id" INTEGER PRIMARY KEY AUTOINCREMENT,
            "info" TEXT
            );
            """)
base.commit()

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.reply(f"Assalomu Aleykum {message.from_user.username} start berganingiz uchun rahmat")


@dp.message_handler()
async def echo(message: types.Message):
    global cur, base
    bot_mes = message.text
    mess = f"User>{message.from_user.username},Time{datetime.now().hour}:" \
        f"{datetime.now().minute}:{datetime.now().second},Message:{message.text}"
    print(mess)
    cur.execute(f"""INSERT INTO Malumotlar(info)
    VALUES({bot_mes});
    """)
    base.commit()
    await message.answer(message.text)



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)

