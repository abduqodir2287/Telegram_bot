import logging
from aiogram import *
from API_examples.api_key import exampe_bot_token
from API_examples.api_telbot_class import helperDB
from buttons_api import menu
from api_cars_bot import cars
# from celebrites_bot import celebrities
# from city_Api_bot import city
# from weather_api_bot import weather
# from country_api import country
# from qr_mes import ITPark
# from world_time import world_time

bot = Bot(token=exampe_bot_token)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

base = helperDB("All_api.db")

@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    print(message.from_user.username)
    await message.answer(f"Assalomu Aleykum {message.from_user.username} botga xush kelibsiz")
    await message.answer("Siz bu yerda xar xil narsalar\n"
                         "Xaqida ma'lumot olishingiz mumkin\n"
                         "Shunchaki shulardan birini tanlang👇👇", reply_markup=menu)
    base.add_item(message.from_user.id, message.from_user.username)

@dp.message_handler()
async def all_api(message: types.Message):
    print("Success")
    print(message.text)
    if message.text == "Mashinalar":
        print(message.text)
        await cars(message)

    # elif message.text == "Mashxurlar":
    #     print(message.text)
    #     await celebrities(message)
    #
    # elif message.text == "Davlatlar":
    #     print(message.text)
    #     await country(message)
    #
    # elif message.text == "Shaxarlar":
    #     print(message.text)
    #     await city(message)
    #
    # elif message.text == "Ob-havo":
    #     print(message.text)
    #     await weather(message)
    #
    #
    # elif message.text == "Jahon vaqti":
    #     print(message.text)
    #     await world_time(message)
    #
    # elif message.text == "ITPark_bot":
    #     print(message.text)
    #     await ITPark(message)

    else:
        await message.reply("Bunday buyruq mavjud emas\n"
                            "Shulardan birini tanlang 👇👇")


async def on_startup(dp: Dispatcher):
    base.create_table()
    print('Bot ishga tushdi ')

async def on_shutdown(dp: Dispatcher):
    print("Good bye!")
    base.log_out()

if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown, skip_updates=True)

