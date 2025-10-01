from dotenv import load_dotenv
from aiogram import Dispatcher, Bot, Router
from aiogram.fsm.storage.redis import RedisStorage, DefaultKeyBuilder
import os
import asyncio
from app.handlers import handler_router
from app.dialogs import dialog_router
from aiogram_dialog import setup_dialogs

load_dotenv()

token = os.getenv("BOT_TOKEN")
redis_url = os.getenv("REDIS_URL") 

storage = RedisStorage.from_url(
    redis_url,
    key_builder=DefaultKeyBuilder(with_destiny=True)
)
bot = Bot(token=token)

dp = Dispatcher(storage=storage)

setup_dialogs(dp)

async def main():
    dp.include_router(router=handler_router)
    dp.include_router(router=dialog_router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())