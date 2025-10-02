from dotenv import load_dotenv
from aiogram_dialog import Window, Dialog, DialogManager
from aiogram_dialog.widgets.kbd import Button, Group
from aiogram_dialog.widgets.text import Const, Format
from aiogram_dialog.widgets.media import DynamicMedia
from aiogram_dialog.api.entities import MediaAttachment, MediaId
from aiogram import Router
from aiogram.enums import ContentType
import os
import redis.asyncio as redis
from app.states import MainMenuDialogStates, RegistrationDialogStates, UpdateUserdataStates
from app.dialog_functions import (
    main_menu_registration, main_menu_support, support_back,
    main_menu_logout, update_data_change,
)
from aiogram.types import CallbackQuery
from app.BotDbManager import Manager

main_menu_router = Router()

db_manager = Manager()

load_dotenv()

redis_url = os.getenv("REDIS_URL", "redis://localhost:6379/0")

redis_db = redis.from_url(redis_url, decode_responses=True)

async def get_main_menu_data(dialog_manager: DialogManager, **kwargs):

    event = dialog_manager.event
    if (isinstance(event, CallbackQuery)):
        user_id = event.from_user.id
    else:
        user_id = event.from_user.id if event.from_user else None
    
    userdata = db_manager.get_user(user_id)
    photo_id = "AgACAgIAAxkDAANBaNkRfGNh9I0vplwzdhjWzRcdQtEAAo78MRsZXshKYAtPuUbhJdMBAAMCAAN5AAM2BA"
    photo = MediaAttachment(ContentType.PHOTO, file_id=MediaId(photo_id))

    is_registered = userdata is not None 
    return {
        "userdata": userdata,
        "photo": photo,
        "is_registered": is_registered
    }

main_menu_dialog = Dialog(
    Window(
        Const("Главное меню"),
        Format(
            "Добро пожаловать, {userdata.surname} {userdata.name} {userdata.patronymic}",
            when=lambda data, w, h: data["is_registered"]
        ),
        DynamicMedia("photo"),
        Group(
            Button(
                Const("Регистрация"), 
                id="main_menu_registration", 
                on_click=main_menu_registration,
                when=lambda data, w, h: not data["is_registered"]
            ),

            Button(
                Const("Выйти"), 
                id="main_menu_logout", 
                on_click=main_menu_logout,
                when=lambda data, w, h: data["is_registered"]
            ),
            Button(
                Const("Изменить данные"), 
                id="update_data_change", 
                on_click=update_data_change,
                when=lambda data, w, h: data["is_registered"]
            ),
            Button(Const("Поддержка"), id="main_menu_support", on_click=main_menu_support),
        ),
        state=MainMenuDialogStates.main_menu,
        getter=get_main_menu_data
    ),
    Window(
        Const("Поддержка"),
        Button(Const("Назад"), id="support_back", on_click=support_back),
        state=MainMenuDialogStates.support
    )
)

main_menu_router.include_router(main_menu_dialog)
