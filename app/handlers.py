from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram_dialog import DialogManager
from app.dialogs import MainMenuDialogStates, RegistrationDialogStates
from aiogram.filters import StateFilter
from aiogram.fsm.storage.redis import RedisStorage
from dotenv import load_dotenv
import os
import redis.asyncio as redis

load_dotenv()

async def save_user_fio(user_id: int, name: str, surname: str, patronymic: str):
    key=f"user:{user_id}"
    await redis_db.hset(key, mapping={
        "name": name,
        "surname": surname,
        "patronymic": patronymic
    })


redis_url = os.getenv("REDIS_URL", "redis://localhost:6379/0")

redis_db = redis.from_url(redis_url, decode_responses=True)

handler_router = Router()

@handler_router.message(StateFilter(RegistrationDialogStates.fio))
async def get_surname(message: Message):
    await message.answer("Введи фамилию:")