# from dotenv import load_dotenv
# from aiogram_dialog import Window, Dialog, DialogManager
# from aiogram_dialog.widgets.kbd import Button, Group
# from aiogram_dialog.widgets.input import TextInput
# from aiogram_dialog.widgets.text import Const, Format
# from aiogram_dialog.widgets.media import DynamicMedia
# from aiogram_dialog.api.entities import MediaAttachment, MediaId
# from aiogram import Router
# from aiogram.enums import ContentType
# from aiogram.fsm.storage.redis import RedisStorage, DefaultKeyBuilder
# import os
# import redis.asyncio as redis
# from .states import MainMenuDialogStates, RegistrationDialogStates, UpdateUserdataStates
# from .dialog_functions import (
#     main_menu_registration, main_menu_support, support_back,
#     reg_info_next, reg_info_cancel, fio_next, fio_cancel,
#     confirm_data_send, confirm_data_change, confirm_data_cancel,
#     on_surname_entered, on_name_entered, on_patronymic_entered,
#     main_menu_logout, update_data_change, update_on_surname_entered,
#     update_on_name_entered, update_on_patronymic_entered
# )
# from aiogram.types import CallbackQuery
# from .BotDbManager import Manager

# dialog_router = Router()

# db_manager = Manager()

# async def get_data(**kwargs):
#     image_id = "AgACAgIAAxkDAANBaNkRfGNh9I0vplwzdhjWzRcdQtEAAo78MRsZXshKYAtPuUbhJdMBAAMCAAN5AAM2BA"
#     image = MediaAttachment(ContentType.PHOTO, file_id=MediaId(image_id))
#     return {'photo': image}


# load_dotenv()


# redis_url = os.getenv("REDIS_URL", "redis://localhost:6379/0")

# redis_db = redis.from_url(redis_url, decode_responses=True)

# async def GetUserData(callback: CallbackQuery, button: Button, manager: DialogManager):
#     tg_id = callback.from_user.id
#     await db_manager.get_user(tg_id)

# async def get_main_menu_data(dialog_manager: DialogManager, **kwargs):

#     event = dialog_manager.event
#     if (isinstance(event, CallbackQuery)):
#         user_id = event.from_user.id
#     else:
#         user_id = event.from_user.id if event.from_user else None
    
#     userdata = db_manager.get_user(user_id)
#     photo_id = "AgACAgIAAxkDAANBaNkRfGNh9I0vplwzdhjWzRcdQtEAAo78MRsZXshKYAtPuUbhJdMBAAMCAAN5AAM2BA"
#     photo = MediaAttachment(ContentType.PHOTO, file_id=MediaId(photo_id))

#     is_registered = userdata is not None 
#     return {
#         "userdata": userdata,
#         "photo": photo,
#         "is_registered": is_registered
#     }

# main_menu_dialog = Dialog(
#     Window(
#         Const("Главное меню"),
#         Format(
#             "Добро пожаловать, {userdata.surname} {userdata.name} {userdata.patronymic}",
#             when=lambda data, w, h: data["is_registered"]
#         ),
#         DynamicMedia("photo"),
#         Group(
#             Button(
#                 Const("Регистрация"), 
#                 id="main_menu_registration", 
#                 on_click=main_menu_registration,
#                 when=lambda data, w, h: not data["is_registered"]
#             ),

#             Button(
#                 Const("Выйти"), 
#                 id="main_menu_logout", 
#                 on_click=main_menu_logout,
#                 when=lambda data, w, h: data["is_registered"]
#             ),
#             Button(
#                 Const("Изменить данные"), 
#                 id="update_data_change", 
#                 on_click=update_data_change,
#                 when=lambda data, w, h: data["is_registered"]
#             ),
#             Button(Const("Поддержка"), id="main_menu_support", on_click=main_menu_support),
#         ),
#         state=MainMenuDialogStates.main_menu,
#         getter=get_main_menu_data
#     ),
#     Window(
#         Const("Поддержка"),
#         Button(Const("Назад"), id="support_back", on_click=support_back),
#         state=MainMenuDialogStates.support
#     )
# )

# registration_dialog = Dialog(
#     Window(
#         Const("Информация о регистрации"),
#         Button(Const("Далее"), id="reg_info_next", on_click=reg_info_next),
#         Button(Const("Отмена"), id="reg_info_cancel", on_click=reg_info_cancel),
#         state=RegistrationDialogStates.reg_info
#     ),
#     Window(
#         Const("Запрос ФИО"),
#         Button(Const("Далее"), id="fio_next", on_click=fio_next),
#         Button(Const("Отмена"), id="fio_cancel", on_click=fio_cancel),
#         state=RegistrationDialogStates.fio
#     ),
#     Window(
#         Const("Введите фамилию: "),
#         TextInput(id="surname_input", on_success=on_surname_entered),
#         state=RegistrationDialogStates.surname
#     ),
#     Window(
#         Const("Введите имя: "),
#         TextInput(id="name_input", on_success=on_name_entered),
#         state=RegistrationDialogStates.name
#     ),
#     Window(
#         Const("Введите отчество: "),
#         TextInput(id="patronymic_input", on_success=on_patronymic_entered),
#         state=RegistrationDialogStates.patronymic
#     ),
#     Window(
#         Const("Подтверждение"),
#         Button(Const("Подтвердить и отправить"), id="confirm_data_send", on_click=confirm_data_send),
#         Button(Const("Изменить"), id="confirm_data_change", on_click=confirm_data_change),
#         Button(Const("Отмена"), id="confirm_data_cancel", on_click=confirm_data_cancel),
#         state=RegistrationDialogStates.confirm_data
#     ),
# )

# confirm_updates_dialog = Dialog(
#     Window(
#         Const("Введите новую фамилию: "),
#         TextInput(id="update_surname_input", on_success=update_on_surname_entered),
#         state=UpdateUserdataStates.surname
#     ),
#     Window(
#         Const("Введите новое имя: "),
#         TextInput(id="update_name_input", on_success=update_on_name_entered),
#         state=UpdateUserdataStates.name
#     ),
#     Window(
#         Const("Введите новое отчество: "),
#         TextInput(id="update_patronymic_input", on_success=update_on_patronymic_entered),
#         state=UpdateUserdataStates.patronymic
#     ),
# )


# dialog_router.include_router(main_menu_dialog)
# dialog_router.include_router(registration_dialog)
# dialog_router.include_router(confirm_updates_dialog)
