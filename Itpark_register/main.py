import logging
from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from Tel_bot_lessons.config import exampe_bot_token

logging.basicConfig(level=logging.INFO)
bot = Bot(token=exampe_bot_token)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


class FSMAdmin(StatesGroup):
    fullname = State()
    phoneNumber = State()
    course = State()
    passport = State()
    saveData = State()


async def start_command(message: types.Message):
    await message.reply('Assalomu aleykum botga hush kelibsiz')
    await FSMAdmin.fullname.set()
    await message.answer('To`liq ismingizni kiriting: ')


async def get_fullname(message: types.Message, state: FSMContext):
    if message.text == 'So`rovni tugatish!':
        await start_command(message)
    else:
        await state.update_data(fullname=message.text.strip())
        await FSMAdmin.next()
        await message.reply("Telefon raqamingizni kiriting(+998...): ")


async def get_PhoneNumber(message: types.Message, state: FSMContext):
    if message.text == 'So`rovni tugatish!':
        await start_command(message)
    else:
        await state.update_data(phoneNumber=message.text.strip())
        await FSMAdmin.next()
        await message.reply("Qanday yo`nalishqa o`qimoqchisiz: ")


async def get_course(message: types.Message, state: FSMContext):
    if message.text == 'So`rovni tugatish!':
        await start_command(message)
    else:
        await state.update_data(course=message.text.strip())
        await FSMAdmin.next()
        await message.answer('Passport rasmini jonating:')


async def get_photo(message: types.Message, state: FSMContext):
    if message.text == 'So`rovni tugatish!':
        await start_command(message)
    else:
        async with state.proxy() as data:
            await message.photo[-1].download(destination_file=f"{data['fullname']}.png", make_dirs=False)
            await state.update_data(passport=message.photo[0].file_id)
            await FSMAdmin.next()
            print('rasm muvaqiyatli saqlandi')


async def register(message: types.Message, state: FSMContext):
    print('################################')
    if message.text == 'So`rovni tugatish!':
        await start_command(message)
    else:
        async with state.proxy() as data:
            print(data["fullname"], data["phoneNumber"], data["course"])
        await state.finish()
    print('111111111111111111')


def register_handler_admin(dp1: Dispatcher):
    dp1.register_message_handler(start_command, commands=['start'], state=None)  # start
    dp1.register_message_handler(get_fullname, state=FSMAdmin.fullname)  # fullname
    dp1.register_message_handler(get_PhoneNumber, state=FSMAdmin.phoneNumber)  # tel
    dp1.register_message_handler(get_course, state=FSMAdmin.course)  # course
    dp1.register_message_handler(get_photo, state=FSMAdmin.passport, content_types="photo")  # photo
    dp1.register_message_handler(register, state=FSMAdmin.saveData)  # save data



if __name__ == '__main__':
    from aiogram import executor
    register_handler_admin(dp)
    executor.start_polling(dp, skip_updates=False)

