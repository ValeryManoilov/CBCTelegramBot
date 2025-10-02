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

import json

with open("app/texts.json", 'r', encoding='utf-8') as file:
    textblock = json.load(file)["main_menu_dialog"]


main_menu_router = Router()

db_manager = Manager()

load_dotenv()

async def get_main_menu_data(dialog_manager: DialogManager, **kwargs):

    event = dialog_manager.event
    if (isinstance(event, CallbackQuery)):
        user_id = event.from_user.id
    else:
        user_id = event.from_user.id if event.from_user else None
    
    userdata = db_manager.get_user(user_id)
    url = "https://fototips.ru/wp-content/uploads/2011/12/landscape_02.jpg"
    photo = MediaAttachment(ContentType.PHOTO, url=url)

    is_registered = userdata is not None 
    return {
        "userdata": userdata,
        "photo": photo,
        "is_registered": is_registered
    }

main_menu_dialog = Dialog(
    Window(
        Const(textblock["main_menu"]["title"]),
        Format(
            f"{textblock["main_menu"]["hello_text"]}\n"
            "{userdata.surname} {userdata.name} {userdata.patronymic}",
            when=lambda data, w, h: data["is_registered"]
        ),
        DynamicMedia("photo"),
        Group(
            Button(
                Const(textblock["main_menu"]["registration"]), 
                id="main_menu_registration", 
                on_click=main_menu_registration,
                when=lambda data, w, h: not data["is_registered"]
            ),

            Button(
                Const(textblock["main_menu"]["exit"]), 
                id="main_menu_logout", 
                on_click=main_menu_logout,
                when=lambda data, w, h: data["is_registered"]
            ),
            Button(
                Const(textblock["main_menu"]["change"]), 
                id="update_data_change", 
                on_click=update_data_change,
                when=lambda data, w, h: data["is_registered"]
            ),
            Button(
                Const(textblock["main_menu"]["support"]), 
                id="main_menu_support", 
                on_click=main_menu_support
            ),
        ),
        state=MainMenuDialogStates.main_menu,
        getter=get_main_menu_data
    ),
    Window(
        Const(textblock["support"]["title"]),
        Const(textblock["support"]["tg_contacts"]),
        Const(textblock["support"]["vk_contacts"]),
        Button(
            Const(textblock["support"]["back"]), 
            id="support_back",
            on_click=support_back),
        state=MainMenuDialogStates.support
    )
)

main_menu_router.include_router(main_menu_dialog)
