from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command

r = Router()

@r.message(Command("help"))
async def help_cmd():
    pass

@r.message(Command("new_games"))
async def new_games_cmd():
    pass