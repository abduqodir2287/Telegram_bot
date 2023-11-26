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
    await message.answer("Siz bu yerda mashxur insonlar\n"
                         "Xaqida ma'lumot olishingiz mumkin\n"
                         "Shunchaki Ismni yozing👇👇👇")


# @dp.message_handler()
# async def celebrities(message: types.Message):
#     api_url = f"https://api.api-ninjas.com/v1/celebrity?name={message.text}"
#     response = requests.get(api_url, headers={"X-Api-Key": key})
#     if response.status_code == requests.codes.ok and response.text != "[]":
#         await message.reply(f"{message.text.capitalize()} xaqida ma'lumotlar👇👇\n"
#                             f"👇👇👇👇👇👇👇👇👇👇👇👇👇👇\n"
#                             f"{response.text}")
#     else:
#         await message.answer("Bunday mashxur inson topilmadi\n"
#                              "Yana bir bor urunib ko'ring")

info = [{"name": "cristiano ronaldo",
         "net_worth": 500000000, "gender": "male", "nationality": "pt",
         "occupation": ["fooball_player", "fashion_entrepreneur"],
         "height": 1.85, "birthdaty": "1985-02-05",
         "age": 38, "is_alive": "true"}]

@dp.message_handler()
async def celebrities(message: types.Message):
    print("Celebrites")
    api_url = f"https://api.api-ninjas.com/v1/celebrity?name={message.text}"
    response = requests.get(api_url, headers={"X-Api-Key": key})
    data = json.loads(response.text)
    for i in data:
        if response.status_code == requests.codes.ok and response.text != "[]":
            await message.reply(f"{message.text.capitalize()} xaqida ma'lumotlar👇👇\n"
                                f"👇👇👇👇👇👇👇👇👇👇👇👇👇👇\n"
                                f"Ismi:{i.get('name')}, Davlat:{i.get('nationality')}, Kasbi:{i.get('occupation')}\n"
                                f"Bo'yi:{i.get('height')}, Tug'ilgan sana:{i.get('birthday')}, Yoshi:{i.get('age')}")
        else:
            await message.answer("Bunday mashxur inson topilmadi\n"
                                 "Yana bir bor urunib ko'ring")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

