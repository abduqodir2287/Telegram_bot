import logging
from aiogram import *

from config import exampe_bot_token

bot = Bot(token=exampe_bot_token)
logging.basicConfig(level=logging.INFO)
dp = Dispatcher(bot)

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





if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=False)
