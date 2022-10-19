from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import callback_data

menyuPython = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Python', callback_data='cources'),
            InlineKeyboardButton(text='Kitoblar', callback_data='book')
        ],
        [
            InlineKeyboardButton(text="Instagramga o'tish", url='https://www.instagram.com/alimardon_boqijonov/')
        ],
        [
            InlineKeyboardButton(text='Search', switch_inline_query_current_chat=''),
            InlineKeyboardButton(text='Ulashish', switch_inline_query="Zo'r Bot Ekan"),
        ],
    ],
)

courceMenu = InlineKeyboardMarkup(row_width=3)
python = InlineKeyboardButton(text='1-dars')
courceMenu.insert(python)