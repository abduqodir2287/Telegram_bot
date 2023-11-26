from aiogram import *

import logging

from config import exampe_bot_token

from aiogram.types import InputFile

from buttons import fileTypesMenu

bot = Bot(token=exampe_bot_token)

dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.answer(f"Assalomu Aleykum {message.from_user.username}\n "
                         f"Start berganingiz uchun rahmat", reply_markup=fileTypesMenu)
rasm = "D:\IT dars\photo_2023-11-04_13-59-26.jpg"

@dp.message_handler()
async def echo(message: types.Message):
    user_id = message.from_user.id
    image = InputFile("D:\IT dars\photo_messi.jpg")
    video = InputFile('D:\IT dars\IMG_7536.MP4')
    doc = InputFile("D:\IT dars\Git commands.docx")
    music = InputFile("D:\IT dars\Danza.mp3.mp3")
    mem = InputFile("D:\IT dars\Screenshot 2023-10-31 154802.png")

    if message.text == 'image':
        await message.bot.send_photo(chat_id=user_id, photo=image)
        print("Success")

    elif message.text == "video":
        await message.bot.send_video(chat_id=user_id, video=video)
        print("Success")

    elif message.text == "document":
        await message.bot.send_document(chat_id=user_id, document=doc)
        print("Success")

    elif message.text == "music":
        await message.bot.send_audio(chat_id=user_id, audio=music)
        print("Success")

    else:
        await message.bot.send_photo(chat_id=user_id, photo=mem)
        await message.reply("Bunday buyruq mavjud emas")
        print("Success")



if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=False)

