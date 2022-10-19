import logging
from distutils.cmd import Command

from aiogram.types import Message, ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton, CallbackQuery
from aiogram import Dispatcher, Bot, executor
from config import TOKEN
from startKeyboard import menuStart, menuKurs, menuRegister, menuProgram, menuFront
from inlineKeyboard import menyuPython, courceMenu


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands="start")
async def start(message: Message):
    await message.answer(f"Assalomu-alaykum, {message.from_user.full_name}!\n"
                         f"Online Kurslarimizga hush kelibsiz", reply_markup=menuStart)


@dp.message_handler(commands="help")
async def start(message: Message):
    await message.answer(f"Assalomu-alaykum, {message.from_user.full_name}!\n"
                         f"Yordam uchun https://t.me/Alimardon_Boqijonov ga yozing")


@dp.message_handler(text='Kurslar')
async def kurlar(message: Message):
    await message.answer("Kursni tanlang!", reply_markup=menuKurs)


@dp.message_handler(text='Biz Haqimizda')
async def kurlar(message: Message):
    await message.answer(f"Biz 2022-yil 17-oktabr sanasida tashkil topganmiz.\n"
                         f"Bizning instagram sahifamiz: https://www.instagram.com/alimardon_boqijonov/")


@dp.message_handler(text="Ro'yxatdan o'tish")
async def register(message: Message):
    await message.answer("Iltimos contact va manzilingizni yuboring!🤗", reply_markup=menuRegister)


@dp.message_handler(text='Orqaga')
async def orqaga(message: Message):
    await message.answer("Kursni tanlang!", reply_markup=menuStart)


@dp.message_handler(text='Bosh Menu')
async def orqaga(message: Message):
    await message.answer("Kursni tanlang!", reply_markup=menuStart)

@dp.message_handler(text='Programming')
async def orqaga(message: Message):
    await message.answer("Dasturlash tilini tanlang!", reply_markup=menuProgram)

@dp.message_handler(text='FrontEnd')
async def orqaga(message: Message):
    await message.answer("FrontEnd Kurslari!", reply_markup=menuFront)

@dp.message_handler(text='Python')
async def python(message: Message):
    await message.answer("Darsni tanlang", reply_markup=menyuPython)

@dp.callback_query_handler(text="Python")
async def python(call: CallbackQuery):
    await call.message.answer("Darsni tanlang", reply_markup=courceMenu)
    await call.answer(cache_time=60)

if __name__ == '__main__':
    executor.start_polling(dp)
