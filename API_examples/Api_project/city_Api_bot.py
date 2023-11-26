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
    await message.answer("Siz bu yerda Shaxarlar\n"
                         "Xaqida ma'lumot olishingiz mumkin\n"
                         "Shunchaki shaxar nomini yozing👇👇👇")



info = [{"name": "Tashkent", "latitude": 41.3, "longitude": 69.2667,
        "country": "UZ", "population": 2424100, "is_capital": "true"}]

@dp.message_handler()
async def city(message: types.Message):
    print("City")
    api_url = f'https://api.api-ninjas.com/v1/city?name={message.text}'
    response = requests.get(api_url, headers={"X-Api-Key": key})
    data = json.loads(response.text)
    for i in data:
        if response.status_code == requests.codes.ok and response.text != "[]":
            await message.reply(f"{message.text.capitalize()} xaqida ma'lumotlar👇👇\n"
                                f"Shaxar:{i.get('name')}, Davlat:{i.get('country')}, Aholi:{i.get('population')}\n"
                                f"Kenglik:{i.get('latitude')}, Uzunlik:{i.get('longitude')},"
                                f" Poytaxt:{i.get('is_capital')}")
        else:
            await message.answer("Bunday Shaxar topilmadi\n"
                                 "Yana bir bor urunib ko'ring")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

