import logging

from aiogram import Bot, Dispatcher, executor, types

from config import exampe_bot_token

from random import *

from db_sql.bot_class import helperDB

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=exampe_bot_token)
dp = Dispatcher(bot)

data = helperDB("Oyin.db")

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer(f"Salom botimizga xush kelibsiz\n"
                         f"Oyinni boshlash uchun '/boshladik deb yozing'")
    data.add_item(message.from_user.id, message.from_user.username)


@dp.message_handler(commands=["boshladik"])
async def oyin(message: types.Message):
    a = randint(1, 20)
    b = randint(1, 20)

    await message.answer(f"{a}+{b}=?")

    if int(message.text) == a + b:
        await message.answer("Correct")
    else:
        await message.answer("Incorrect")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
