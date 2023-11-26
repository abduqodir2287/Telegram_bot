import logging
from aiogram import *
from API_examples.api_key import key, exampe_bot_token
import requests
import json

bot = Bot(token=exampe_bot_token)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    print(message.from_user.username)
    await message.answer(f"Assalomu Aleykum {message.from_user.username} botga xush kelibsiz")
    await message.answer("Siz bu yerda xoxlagan shaxringizning\n"
                         "Vaqti xaqida ma'lumot olishingiz mumkin\n"
                         "Shunchaki Shaxar nomini yozing👇👇👇")

@dp.message_handler()
async def world_time(message: types.Message):
    print("Time")
    api_url = f'https://api.api-ninjas.com/v1/worldtime?city={message.text}'
    response = requests.get(api_url, headers={'X-Api-Key': key})
    data = json.loads(response.text)
    if response.status_code == requests.codes.ok and response.text != "[]":
        await message.reply(f"{message.text} xaqida ma'lumotlar 👇👇\n"
                            f"Vaqt zonasi:{data.get('timezone')}, Sana va vaqt:{data.get('datetime')}\n"
                            f"Xafta kuni:{data.get('day_of_week')}")

    else:
        await message.answer("Bunday Shaxar topilmadi\n"
                             "Yana bir bor urunib ko'ring")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
