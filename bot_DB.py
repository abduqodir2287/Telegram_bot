from aiogram import *

from logging import *

from config import exampe_bot_token

from datetime import *

from db_sql.bot_class import Helperbotdb


bot = Bot(token=exampe_bot_token)
basicConfig(level=INFO)
dp = Dispatcher(bot)

base = Helperbotdb("Example_bot.db")
base.create_table("Ban_users")


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.reply(f"Assalomu Aleykum {message.from_user.username} start berganingiz uchun rahmat")


@dp.message_handler(commands=['block_list'])
async def block(message: types.Message):
    await message.reply(f"Bloklangan userlar ro'yxati\n"
                        f"{base.select_item()}")
    print("Success")


@dp.message_handler()
async def echo(message: types.Message):
    global base
    mess = f"User>{message.from_user.username},Time{datetime.now().hour}:" \
        f"{datetime.now().minute}:{datetime.now().second},Message:{message.text}"
    print(mess)
    for i in base.select_item():
        if message.from_user.id in i and message.text != "/block_list":
            await message.delete()

    if 'http' in message.text:
        base.add_item(message.from_user.id)
        await message.answer("Reklama tarqatmang")
        await message.delete()



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)