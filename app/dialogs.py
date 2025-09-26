from aiogram_dialog import Window, Dialog
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.text import Const
from aiogram_dialog.widgets.media import DynamicMedia
from aiogram import Router
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager

dialog_router = Router()

class MainMenuDialogStates(StatesGroup):
    main_menu = State()
    support = State()

class RegistrationDialogStates(StatesGroup):
    reg_info = State()
    fio = State()
    confirm_data = State()

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
    await manager.start(RegistrationDialogStates.confirm_data)

async def fio_cancel(callback: CallbackQuery, button: Button, manager: DialogManager):
    await manager.start(MainMenuDialogStates.main_menu)


async def confirm_data_send(callback: CallbackQuery, button: Button, manager: DialogManager):
    await manager.start(MainMenuDialogStates.main_menu)

async def confirm_data_change(callback: CallbackQuery, button: Button, manager: DialogManager):
    await manager.start(RegistrationDialogStates.fio)

async def confirm_data_cancel(callback: CallbackQuery, button: Button, manager: DialogManager):
    await manager.start(MainMenuDialogStates.main_menu)


main_menu_dialog = Dialog(
    Window(
        Const("Главное меню"),
        Button(Const("Регистрация"), id="main_menu_registration", on_click=main_menu_registration),
        Button(Const("Поддержка"), id="main_menu_support", on_click=main_menu_support),
        state=MainMenuDialogStates.main_menu
    ),
    Window(
        Const("Поддержка"),
        Button(Const("Назад"), id="support_back", on_click=support_back),
        state=MainMenuDialogStates.support
    )
)


registration_dialog = Dialog(
    Window(
        Const("Информация о регистрации"),
        Button(Const("Далее"), id="reg_info_next", on_click=reg_info_next),
        Button(Const("Отмена"), id="reg_info_cancel", on_click=reg_info_cancel),
        state=RegistrationDialogStates.reg_info
    ),
    Window(
        Const("Запрос ФИО"),
        Button(Const("Далее"), id="fio_next", on_click=fio_next),
        Button(Const("Отмена"), id="fio_cancel", on_click=fio_cancel),
        state=RegistrationDialogStates.fio
    ),
    Window(
        Const("Подтверждение"),
        Button(Const("Подтвердить и отправить"), id="confirm_data_send", on_click=confirm_data_send),
        Button(Const("Изменить"), id="confirm_data_change", on_click=confirm_data_change),
        Button(Const("Отмена"), id="confirm_data_cancel", on_click=confirm_data_cancel),
        state=RegistrationDialogStates.confirm_data
    ),
)

dialog_router.include_router(main_menu_dialog)
dialog_router.include_router(registration_dialog)