from aiogram.types import *

btn1 = KeyboardButton("QRcode")

but_cars = KeyboardButton("Mashinalar")
but_celebrity = KeyboardButton("Mashxurlar")
but_country = KeyboardButton("Davlatlar")
but_city = KeyboardButton("Shaxarlar")
but_weather = KeyboardButton("Ob-havo")
but_time = KeyboardButton("Jahon vaqti")
but_bot = KeyboardButton("ITPark_bot")


menu = ReplyKeyboardMarkup(resize_keyboard=True).add(but_cars, but_celebrity)\
    .add(but_country, but_city).add(but_weather, but_time).add(but_bot)


