from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button
from .states import MainMenuDialogStates, RegistrationDialogStates
from aiogram_dialog import DialogManager
from aiogram.types import Message
from aiogram_dialog.widgets.input import TextInput
import redis.asyncio as redis
import os
from .BotDbManager import Manager
from .user import User

db_manager = Manager()

async def main_menu_registration(callback: CallbackQuery, button: Button, manager: DialogManager):
    await manager.start(RegistrationDialogStates.reg_info)

async def main_menu_support(callback: CallbackQuery, button: Button, manager: DialogManager):
    await manager.switch_to(MainMenuDialogStates.support)

async def support_back(callback: CallbackQuery, button: Button, manager: DialogManager):
    await manager.switch_to(MainMenuDialogStates.main_menu)


async def reg_info_next(callback: CallbackQuery, button: Button, manager: DialogManager):
    await manager.switch_to(RegistrationDialogStates.fio)

async def reg_info_cancel(callback: CallbackQuery, button: Button, manager: DialogManager):
    await manager.start(MainMenuDialogStates.main_menu)

async def fio_next(callback: CallbackQuery, button: Button, manager: DialogManager):
    await manager.switch_to(RegistrationDialogStates.surname)

async def fio_cancel(callback: CallbackQuery, button: Button, manager: DialogManager):
    await manager.start(MainMenuDialogStates.main_menu)



redis_url = os.getenv("REDIS_URL", "redis://localhost:6379/0")

redis_db = redis.from_url(redis_url, decode_responses=True)


async def confirm_data_send(callback: CallbackQuery, button: Button, manager: DialogManager):
    tg_id = callback.from_user.id
    data = manager.dialog_data
    
    new_user = User(
        telegram_id=tg_id,
        surname=data["surname"],
        name=data["name"],
        patronymic=data["patronymic"]
    )

    db_manager.add_user(new_user)
    await callback.message.answer("Все сохранено")
    await manager.done()
    await manager.start(MainMenuDialogStates.main_menu)

async def confirm_data_change(callback: CallbackQuery, button: Button, manager: DialogManager):
    await manager.start(RegistrationDialogStates.fio)

async def confirm_data_cancel(callback: CallbackQuery, button: Button, manager: DialogManager):
    await manager.start(MainMenuDialogStates.main_menu)

async def on_surname_entered(message: Message, widget: TextInput, manager: DialogManager, text: str):
    manager.dialog_data.update({"surname": text})
    await message.answer(f"Фамилия сохранена: {text}")
    await manager.switch_to(RegistrationDialogStates.name)

async def on_name_entered(message: Message, widget: TextInput, manager: DialogManager, text: str):
    manager.dialog_data.update({"name": text})
    await message.answer(f"Имя сохранено: {text}")
    await manager.switch_to(RegistrationDialogStates.patronymic)

async def on_patronymic_entered(message: Message, widget: TextInput, manager: DialogManager, text: str):
    manager.dialog_data.update({"patronymic": text})
    await message.answer(f"Отчество сохранено: {text}")
    await manager.switch_to(RegistrationDialogStates.confirm_data)