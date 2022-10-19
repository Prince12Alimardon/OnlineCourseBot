from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menuStart = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Kurslar'),
            KeyboardButton(text='Biz Haqimizda'),
            KeyboardButton(text="Ro'yxatdan o'tish"),
        ],
    ],
    resize_keyboard=True
)
menuKurs = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Programming'),
            KeyboardButton(text='FrontEnd'),
            KeyboardButton(text='BackEnd'),
            KeyboardButton(text='Android'),
            KeyboardButton(text='Data Science'),
        ],
        [
            KeyboardButton(text='Orqaga'),
            KeyboardButton(text='Bosh Menu'),
        ]
    ],
    resize_keyboard=True
)
menuRegister = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Contact', request_contact=True),
            KeyboardButton(text='Location', request_location=True),
        ],
    ],
    resize_keyboard=True
)
menuProgram = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Python'),
            KeyboardButton(text='Java'),
            KeyboardButton(text='GoLang'),
        ],
    ],
    resize_keyboard=True
)
menuFront = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='HTML5'),
            KeyboardButton(text='CSS3'),
            KeyboardButton(text='Javascript'),
        ],
        [
            KeyboardButton(text='ReactJS'),
            KeyboardButton(text='NodeJS'),
            KeyboardButton(text='AngularJS'),
        ],
    ],
    resize_keyboard=True
)