import logging
import requests
import json
from PIL import Image, ImageDraw, ImageFont
from aiogram import *
from aiogram.types import InputFile
from api_key import exampe_bot_token

bot = Bot(token=exampe_bot_token)
logging.basicConfig(level=logging.INFO)
dp = Dispatcher(bot)
font = ImageFont.truetype("arial.ttf", size=30)

@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.answer(f"Assalomu Aleykum {message.from_user.username} botga xush kelibsiz")
    await message.answer("Siz bu yerda Qur'on suralarini oqishingiz mumkin\n"
                         "Sura raqamini yozing👇👇")

@dp.message_handler()
async def text(message: types.Message):
    url = f"https://al-quran1.p.rapidapi.com/{message.text}"
    headers = {
        "X-RapidAPI-Key": "48ec87fe45mshecb35adf6cb2136p11cf43jsn838685d94fd2",
        "X-RapidAPI-Host": "al-quran1.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    dic1 = data['verses']
    for i in dic1:
        img = Image.new("RGBA", (640, 640), "white")
        draw = ImageDraw.Draw(img)
        draw.text((400, 400), text=dic1[i]["content"], fill="black", font=font)
        photo = InputFile(img)
        await message.bot.send_photo(chat_id=message.from_user.id)



