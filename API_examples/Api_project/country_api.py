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
    await message.answer("Siz bu yerda barcha davlatlar\n"
                         "Xaqida ma'lumot olishingiz mumkin\n"
                         "Shunchaki Davlat nomini yozing👇👇👇")


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

info = ('[{"gdp": 50500.0, "sex_ratio": 99.6, "surface_area": 448969.0, '
         '"life_expectancy_male": 69.4, "unemployment": 6.1, "imports": 21867.0, '
         '"homicide_rate": 1.1, "currency": {"code": "UZS", "name": "Uzbekistan Sum"}, '
         '"iso2": "UZ", "employment_services": 46.8, "employment_industry": 29.9, '
         '"urban_population_growth": 1.5, "secondary_school_enrollment_female": 92.7, '
         '"employment_agriculture": 23.3, "capital": "Tashkent", "co2_emissions": '
         '81.2, "forested_area": 7.6, "tourists": 5346.0, "exports": 14930.0, '
         '"life_expectancy_female": 73.6, "post_secondary_enrollment_female": 8.2, '
         '"post_secondary_enrollment_male": 11.8, "primary_school_enrollment_female": '
         '103.4, "infant_mortality": 20.8, "gdp_growth": 5.1, "threatened_species": '
         '62.0, "population": 33469.0, "urban_population": 50.4, '
         '"secondary_school_enrollment_male": 93.9, "name": "Uzbekistan", '
         '"pop_growth": 1.6, "region": "Central Asia", "pop_density": 78.7, '
         '"internet_users": 55.2, "gdp_per_capita": 1555.0, "fertility": 2.4, '
         '"refugees": 95.9, "primary_school_enrollment_male": 105.0}]')

@dp.message_handler()
async def country(message: types.Message):
    print("Country")
    api_url = f'https://api.api-ninjas.com/v1/country?name={message.text}'
    response = requests.get(api_url, headers={'X-Api-Key': key})
    data = json.loads(response.text)
    for i in data:
        if response.status_code == requests.codes.ok and response.text != "[]":
            await message.reply(f"{message.text.capitalize().strip()} xaqida ma'lumotlar👇👇\n"
                                f"Davlat nomi:{i.get('name')}, Import:{i.get('imports')}, Poytaxt:{i.get('capital')}\n"
                                f"Valyuta:{i.get('currency').get('code', 'name')}, Region:{i.get('region')}\n"
                                f"Export:{i.get('exports')}, Aholi:{i.get('population')}, YaIM:{i.get('gdp')}")
        else:
            await message.answer("Bunday Davlat topilmadi\n"
                                 "Yana bir bor urunib ko'ring")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
