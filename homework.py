from aiogram import *

from logging import *

from config import exampe_bot_token

from datetime import *


bot = Bot(token=exampe_bot_token)
basicConfig(level=INFO)
dp = Dispatcher(bot)

ban_list = []

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.reply(f"Assalomu Aleykum {message.from_user.username} start berganingiz uchun rahmat")


@dp.message_handler(commands=['block_list'])
async def block(message: types.Message):
    await message.reply(f"Bloklangan userlar ro'yxati\n"
                        f"{ban_list}")
    print("Success")


@dp.message_handler()
async def echo(message: types.Message):
    global ban_list
    mess = f"User>{message.from_user.id},Time{datetime.now().hour}:" \
        f"{datetime.now().minute}:{datetime.now().second},Message:{message.text}"
    print(mess)

    if message.from_user.id in ban_list and message.text != "/block_list":
        await message.delete()

    if 'http' in message.text:
        ban_list.append(message.from_user.id)
        await message.answer("Reklama tarqatmang")
        await message.delete()



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)


