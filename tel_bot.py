from aiogram import *

from buttons import menu

import logging

from config import exampe_bot_token

logging.basicConfig(level=logging.INFO)

bot = Bot(token=exampe_bot_token)

dp = Dispatcher(bot)

links = {"Python": "https://youtu.be/_uQrJ0TkZlc?si=sxzqw0Uw-UezGDh9",
         "Java": "https://youtu.be/VHbSopMyc4M?si=c4aQj5eW35_2wpra",
         "JavaScript": "https://youtu.be/fcMcf_4PjfI?si=-dJmvuuzlyXkKMZp",
         "C++": "https://youtu.be/EKifZWIdNgM?si=sWUcNztZ2q_NzNs0",
         "C#": "https://youtu.be/EKifZWIdNgM?si=sWUcNztZ2q_NzNs0",
         "Ruby": "https://youtu.be/t_ispmWmdjY?si=Pj0vi4S6m7UCqAqs",
         "PHP": "https://youtu.be/wvIV5BtS3lY?si=HP-D_x9lSXXKwpgu",
         "GO": "https://youtu.be/un6ZyFkqFKo?si=-p1nf9v5niL6GK2j"
         }


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply("Assalomu aleykum botga xush kelibsiz", reply_markup=menu)


@dp.message_handler()
async def echo(message: types.Message):
    if message.text is None:
        await message.answer("Bu buyruq mavjud emas")
    else:
        await message.answer(links.get(message.text))



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)


