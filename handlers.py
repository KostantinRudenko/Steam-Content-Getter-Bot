from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

from web_parser import WebParser

r = Router()
parser = WebParser()

class Count(StatesGroup):
    count = State()

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
    games = parser.get_new()
    for i in range(0, count):
        ans_msg = ""
        for key, value in games[i].items():
            ans_msg = ans_msg + f"{key}: " + value + "\n"
        await message.answer(ans_msg)