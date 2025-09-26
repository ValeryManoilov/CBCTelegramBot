from dotenv import load_dotenv
from aiogram import Dispatcher, Bot
import os
import asyncio

load_dotenv()

token = os.getenv("BOT_TOKEN")

bot = Bot(token=token)

dp = Dispatcher(bot)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())