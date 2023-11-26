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
    await message.answer("Siz bu yerda ob-havo\n"
                         "Xaqida ma'lumot olishingiz mumkin\n"
                         "Shunchaki Shaxar nomini yozing👇👇👇")


weather = ('{"cloud_pct": 99, "temp": 3, "feels_like": -1, "humidity": 83, "min_temp": '
            '1, "max_temp": 4, "wind_speed": 3.76, "wind_degrees": 229, "sunrise": '
            '1699938110, "sunset": 1699968368}')

@dp.message_handler()
async def weather(message: types.Message):
    print("Ob-havo")
    api_url = f'https://api.api-ninjas.com/v1/weather?city={message.text}'
    response = requests.get(api_url, headers={'X-Api-Key': key})
    data = json.loads(response.text)
    if response.status_code == requests.codes.ok and response.text != "[]":
        await message.reply(f"{message.text} xaqida ma'lumotlar 👇👇\n"
                            f"Harorat:{data.get('temp')}, Namlik:{data.get('humidity')}\n"
                            f"Minimum Harorat:{data.get('min_temp')}, Maksimum Harorat:{data.get('max_temp')}\n"
                            f"Shamol tezligi:{data.get('wind_speed')}")
    else:
        await message.answer("Bunday Shaxar topilmadi\n"
                             "Yana bir bor urunib ko'ring")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

