from aiogram.fsm.state import StatesGroup, State

class Count(StatesGroup):
    count = State()

class GameName(StatesGroup):
    game_name = State()