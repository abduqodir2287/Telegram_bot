import logging

from aiogram import *
from aiogram.types import KeyboardButton

from config import exampe_bot_token
from first_tel_bot import links
from buttons import menu

bot = Bot(token=exampe_bot_token)

dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)

num = 1
button = KeyboardButton(f"btn")


@dp.message_handler(commands=["start"])
async def start_com(message: types.Message):
    user_info = message.from_user.username

    await message.reply(f"Assalomu Aleykum {user_info} botga xush kelibsiz\n"
                        f"Dasturlash tilini tanlang", reply_markup=menu)


@dp.message_handler()
async def add_btn(message: types.Message):
    global button

    if message.text == "ADD":
        menu.add(button)
        await message.answer("Button qoshish uchun /start ni bosing")
    else:
        await message.answer(links.get(message.text))


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)


