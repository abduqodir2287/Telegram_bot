import logging
from aiogram import Bot, Dispatcher, executor, types
from Tel_bot_lessons.config import exampe_bot_token
from bot_class import helperDB

logging.basicConfig(level=logging.INFO)

bot = Bot(token=exampe_bot_token)
dp = Dispatcher(bot)

conn = helperDB("DataStorage.db")



@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply('Assalomu aleykum botga hush kelibsiz')
    data = conn.select_item()
    info = (int(message.from_user.id), message.from_user.username)
    if info not in data:
        conn.add_item(int(message.from_user.id), message.from_user.username)
        print("added")
    else:
        await message.answer("Siz botga start berib bolgansiz")
        print("already added")

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

async def on_startup(dp: Dispatcher):
    conn.setup('user_info')
    print('bot ishga tushdi ')
async def on_shutdown(dp: Dispatcher):
    print('Xayr')
    conn.log_out()


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown, skip_updates=False)
