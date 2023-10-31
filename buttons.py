from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


btn1 = KeyboardButton('Python')
btn2 = KeyboardButton('Java')
btn3 = KeyboardButton('JavaScript')
btn4 = KeyboardButton('C++')
btn5 = KeyboardButton('C#')
btn6 = KeyboardButton("Ruby")
btn7 = KeyboardButton("PHP")
btn8 = KeyboardButton("GO")

add_but = KeyboardButton("ADD")


menu = (ReplyKeyboardMarkup(resize_keyboard=True)
        .add(btn1, btn2).add(btn3, btn6).add(btn4, btn5).add(btn7, btn8).add(add_but))

btn_image = KeyboardButton('image')
btn_music = KeyboardButton('music')
btn_video = KeyboardButton('video')
btn_doc = KeyboardButton('document')
fileTypesMenu = (ReplyKeyboardMarkup(resize_keyboard=True).add(btn_image,
        btn_music).add(btn_video, btn_doc))

