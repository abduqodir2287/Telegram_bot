import logging
from aiogram import *
from aiogram.types import InputFile
from API_examples.api_key import exampe_bot_token

bot = Bot(token=exampe_bot_token)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    print(message.from_user.username)
    await message.answer(f"Assalomu Aleykum {message.from_user.username} botga xush kelibsiz")
    await message.answer("Siz bu yerda xoxlagan mashinangiz\n"
                         "Xaqida ma'lumot olishingiz mumkin\n"
                         "Shunchaki mashinaning modelini yozing👇👇👇")

@dp.message_handler()
async def ITPark(message: types.Message):
    await message.bot.send_photo(chat_id=message.from_user.id,
                                 photo=InputFile("D:\IT dars\photo_2023-11-23_23-04-15.jpg"))
    await message.answer("Siz bu QRcode orqali ITParkning rasmiy saytidan\n"
                         "Ro'yxatdan o'tishingiz mumkin")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
