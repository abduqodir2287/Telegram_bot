import logging
from aiogram import Bot, Dispatcher, executor, types
from config import exampe_bot_token
from datetime import *

logging.basicConfig(level=logging.INFO)

ban_list = []
ban_min = []

bot = Bot(token=exampe_bot_token)
dp = Dispatcher(bot)

"""__________________________Client chat______________________________________"""
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply(f'Assalomu aleykum {message.from_user.username} Start berganingiz uchun rahmat!')


"""__________________________Group chat______________________________________"""
@dp.message_handler()
async def qorovul(message: types.Message):
    print(f"DATE: {datetime.now().strftime('%H:%M')} USER: {message.from_user.username} MSG: {message.text}")
    global ban_list, ban_min
    now_hour = datetime.now().hour
    now_min = datetime.now().minute
    now_sec = datetime.now().second

    if 'http' in message.text:
        await message.reply("Reklama tarqatmang!!!")
        await message.delete()
        now_all = f"{message.from_user.username}>>{now_hour}:{now_min}:{now_sec}"
        print(now_all)
        ban_list.append(message.from_user.id)

    if message.from_user.id in ban_list:
        await message.delete()




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)

