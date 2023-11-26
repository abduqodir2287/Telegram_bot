import logging
from aiogram import *
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from ITPark_bot_token import bot_token
from db_sql.itpark_bot_class import Itpark_bot_helperDB
from bot_buttons import *

bot = Bot(token=bot_token)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
logging.basicConfig(level=logging.INFO)

base = Itpark_bot_helperDB("PDP.db")


class FSMAdmin(StatesGroup):
    fullname = State()
    phoneNumber = State()
    course = State()
    photo = State()
    saveData = State()

async def start_command(message: types.Message):
    print(f"{message.from_user.username}")
    await message.reply(f"Assalomu Aleykum {message.from_user.username} PDP educationning rasmiy botiga "
                        f"xush kelibsiz")
    await FSMAdmin.fullname.set()
    await message.answer("To'liq ismingizni kirting: ", reply_markup=cansel_btn)

async def get_fullname(message: types.Message, state: FSMContext):
    if message.text == "So`rovni tugatish!":
        await start_command(message)
        print(f"{message.from_user.username} So'rovni tugatdi")
    else:
        await state.update_data(fullname=message.text.strip())
        await FSMAdmin.next()
        await message.reply("Telefon raqamingizni kiriting (+998): ")

async def get_phoneNumber(message: types.Message, state: FSMContext):
    if message.text == "So`rovni tugatish!":
        await start_command(message)
        print(f"{message.from_user.username} So'rovni tugatdi")
    else:
        await state.update_data(phoneNumber=message.text.strip())
        await FSMAdmin.next()
        await message.reply("Qanday yo'nalishda o'qimoqchisiz: ", reply_markup=menu)

async def get_course(message: types.Message, state: FSMContext):
    if message.text == "So`rovni tugatish!":
        await start_command(message)
        print(f"{message.from_user.username} So'rovni tugatdi")
    else:
        await state.update_data(course=message.text.strip())
        await FSMAdmin.next()
        await message.reply("Rasmingzni jo'nating: ", reply_markup=cansel_btn)


async def get_photo(message: types.Message, state: FSMContext):
    if message.text == "So`rovni tugatish!":
        await start_command(message)
        print(f"{message.from_user.username} So'rovni tugatdi")
    else:
        async with state.proxy() as data:
            await message.photo[-1].download(destination_file=f"{data['fullname']}.png", make_dirs=False)
            await state.update_data(photo=message.photo[0].file_id)
            await FSMAdmin.next()
            print("Rasim muvafaqiyatli saqlandi!")
        await message.reply("Malumotlar uchun rahmat", reply_markup=add_btn)

async def regiter(message: types.Message, state: FSMContext):
    if message.text == "So`rovni tugatish!":
        await start_command(message)
        print(f"{message.from_user.username} So'rovni tugatdi")
    else:
        async with state.proxy() as data:
            print(f"Talabaning malumotlari {data['fullname']}, {data['phoneNumber']}, {data['course']}")
            base.add_item(data["fullname"], data["phoneNumber"], data["course"], data["photo"])
        await state.finish()
        await message.answer("Malumotlar muvofaqiyatli saqlandi")
        await message.answer("Yangi Talaba qo'shish uchun /start deb yozing")


async def register_handler_admin(dp1: Dispatcher):
    dp1.register_message_handler(start_command, commands=["start"])
    dp1.register_message_handler(get_fullname, state=FSMAdmin.fullname)
    dp1.register_message_handler(get_phoneNumber, state=FSMAdmin.phoneNumber)
    dp1.register_message_handler(get_course, state=FSMAdmin.course)
    dp1.register_message_handler(get_photo, state=FSMAdmin.photo)
    dp1.register_message_handler(regiter, FSMAdmin.saveData)

async def on_startup(dp: Dispatcher):
    print("Bot ishga tushdi!")
    base.create_table("Talabalar")

async def on_shutdown(dp: Dispatcher):
    print("Xayr!")
    base.log_out()


if __name__ == "__main__":
    register_handler_admin(dp)
    executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown, skip_updates=False)




