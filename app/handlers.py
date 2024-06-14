from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext

from app.states import Count, GameName
from web_parser import WebParser
from app import keyboards as kbs
from config import *

r = Router()
parser = WebParser()


@r.message(CommandStart())
async def start_cmd(message: Message):
    await message.answer("Hey guy!\nI am Steam Content Getter Bot(or SCG bot)\n")

@r.message(Command('help'))
async def help_cmd(message: Message):
    await message.reply("help")



@r.message(Command("get_new"))
async def get_new_cmd(message: Message, state: FSMContext):
    await state.set_state(Count.count)
    await message.answer("Enter count of games.")

@r.message(Count.count)
async def send_new(message: Message):
    count = int(message.text)
    games = parser.get_new(count)
    for i in range(0, count):
        ans_msg = ""
        for key, value in games[i].items():
            ans_msg = ans_msg + f"{key}: " + value + "\n"
        await message.answer(ans_msg)



@r.message(Command("get_game"))
async def get_game_cmd(message: Message, state: FSMContext):
    await state.set_state(GameName.game_name)
    await message.answer("Enter name of the game which you are interested in.")

@r.message(GameName.game_name)
async def send_keyboard(message: Message, state: FSMContext):
    await state.update_data(game_name = message.text)
    a_elem = parser.is_excists_a("search_result_row ds_collapse_flag", message.text)
    if a_elem != False:
        await message.answer("Choose what do you want to know about this game...",
                            reply_markup=kbs.game_elems_kbrd)
    else:
        await message.answer("Game not found")

@r.callback_query(F.data == DESC_CLBK)
async def send_desc(clbk: CallbackQuery):
    await clbk.answer("Sending of description...")
    desc = parser.get_desc()
    await clbk.message.answer("Description: " + desc)
    
@r.callback_query(F.data == PRICE_CLBK)
async def send_price(clbk: CallbackQuery):
    await clbk.answer("Sending price...")
    await clbk.message.answer("Price: " + parser.get_price())

@r.callback_query(F.data == RELEAS_DATE_CLBK)
async def send_release_date(clbk: CallbackQuery):
    await clbk.answer("Sending release date...")
    await clbk.message.answer(parser.get_date())

@r.callback_query(F.data == DEV_AND_PUBER_CLBK)
async def send_devs(clbk: CallbackQuery):
    await clbk.answer("Sending of developer and publisher...")
    devers = parser.get_devers()
    await clbk.message.answer(devers["dev"] + "\n" + devers["pub"])

@r.callback_query(F.data == REVIEWS_CLBK)
async def send_reviews(clbk: CallbackQuery):
    await clbk.answer("Sending of reviews...")
    res = parser.get_reviews()
    await clbk.message.answer(res["all"] + "\n" + res["nrst"])

@r.callback_query(F.data == BACK_CLBK)
async def back_from_kb(clbk: CallbackQuery):
    await clbk.message.delete()
    await clbk.message.answer("Something else?")