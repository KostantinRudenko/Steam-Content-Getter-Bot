import aiogram
from aiogram import Bot, Dispatcher

from config import *

class Main:
    def __init__(self) -> None:
        self.bot = Bot(TOKEN)
        self.dp = Dispatcher(self.bot)