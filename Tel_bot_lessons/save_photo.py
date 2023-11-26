import logging
from aiogram import *
from aiogram.types import InputFile

from config import exampe_bot_token

bot = Bot(token=exampe_bot_token)
logging.basicConfig(level=logging.INFO)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.answer(f"Assalomu Aleykum {message.from_user.username}\n "
                         f"Start berganingiz uchun rahmat")


# @dp.message_handler(content_types=types.ContentTypes.PHOTO)
# async def save_photo(message: types.Message):
#     photo = message.photo[-1]
#     file_id = photo.file_id
#     file = await bot.get_file(file_id)
#     file_path = file.file_path
#     downloaded_file = await bot.download_file(file_path)
#     with open('saqlangan_rasm.jpg', 'wb') as f:
#         f.write(downloaded_file.read())
#     await message.reply('Rasm saqlandi!')


@dp.message_handler(content_types=types.ContentType.PHOTO)
async def save_photo(message: types.Message):
    photo = message.photo[-1]
    file_id = photo.file_id
    file = await bot.get_file(file_id)
    file_path = file.file_path
    downloaded_file = await bot.download_file(file_path)
    with open("../Saqlangan rasm.jpg", "wb") as f:
        f.write(downloaded_file.read())
    await message.reply("Rasm saqlandi")
    print("Success")


@dp.message_handler()
async def echo(message: types.Message):
    mem = InputFile("D:\IT dars\Screenshot 2023-10-31 154802.png")

    await message.bot.send_photo(chat_id=message.from_user.id, photo=mem)
    await message.reply("Bunday buyruq mavjud emas")
    print("Success")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
