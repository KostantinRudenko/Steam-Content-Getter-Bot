from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)

from config import *

game_elems_kbrd = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Description", callback_data=DESC_CLBK),
        InlineKeyboardButton(text="Price", callback_data=PRICE_CLBK)],
        [InlineKeyboardButton(text="Developer and Publisher", callback_data=DEV_AND_PUBER_CLBK)],
        [InlineKeyboardButton(text="Date of release", callback_data=RELEAS_DATE_CLBK),
        InlineKeyboardButton(text="Reviews", callback_data=REVIEWS_CLBK)],
        [InlineKeyboardButton(text="<< Back", callback_data=BACK_CLBK)]
    ])