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
    await message.answer("Siz bu yerda xoxlagan mashinangiz\n"
                         "Xaqida ma'lumot olishingiz mumkin\n"
                         "Shunchaki mashinaning modelini yozing👇👇👇")

bmw = ('[{"city_mpg": 14, "class": "compact car", "combination_mpg": 15, '
        '"cylinders": 6, "displacement": 2.5, "drive": "rwd", "fuel_type": "gas", '
        '"highway_mpg": 17, "make": "import trade services", "model": "bmw 325i", '
        '"transmission": "a", "year": 1992},]')

@dp.message_handler()
async def cars(message: types.Message):
    print("Cars")
    await message.reply("Mashinaning modelini yozing👇👇👇")

    api_url = f'https://api.api-ninjas.com/v1/cars?model={message.text}'
    response = requests.get(api_url, headers={"X-Api-Key": key})
    data = json.loads(response.text)
    for i in data:
        if response.status_code == requests.codes.ok:
            await message.reply(f"Mashina xaqida ma'lumotlar👇👇\n"
                                f"Изготовление:{i.get('make')}, Модель:{i.get('model')}, Год:{i.get('year')},\n"
                                f"Класс:{i.get('class')},Тип топлива:{i.get('fuel_type')},"
                                f"Цилиндры:{i.get('cylinders')}")
        else:
            await message.answer("Bunday mashina topilmadi\n"
                                 "Yana bir bor urunib ko'ring")
    await cars(message)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

