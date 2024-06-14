import asyncio
from aiogram import Bot, Dispatcher
from app.handlers import r

from config import *

class Main:
    def __init__(self) -> None:
        self.bot = Bot(TOKEN)
        self.dp = Dispatcher()
        self.dp.include_router(r)
    
    async def run_bot(self):
        print("Bot started")
        await self.dp.start_polling(self.bot)

if __name__ == "__main__":
    try:
        main = Main()
        asyncio.run(main.run_bot())
    except KeyboardInterrupt:
        print("Bot stopped")