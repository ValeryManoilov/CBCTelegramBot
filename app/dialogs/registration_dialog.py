
from aiogram_dialog import Window, Dialog
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.input import TextInput
from aiogram_dialog.widgets.text import Const, Format
from aiogram import Router
from app.states import RegistrationDialogStates
from app.dialog_functions import (
    reg_info_next, reg_info_cancel, fio_next, fio_cancel,
    confirm_data_send, confirm_data_change, confirm_data_cancel,
    on_surname_entered, on_name_entered, on_patronymic_entered,
)
from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
import json

with open("app/texts.json", 'r', encoding='utf-8') as file:
    textblock = json.load(file)["registration_dialog"]

registration_router = Router()

registration_dialog = Dialog(
    Window(
        Const(textblock["registr_info"]["title"]),
        Const(textblock["registr_info"]["text"]),
        Button(Const(textblock["registr_info"]["next"]), id="reg_info_next", on_click=reg_info_next),
        Button(Const(textblock["registr_info"]["cancel"]), id="reg_info_cancel", on_click=reg_info_cancel),
        state=RegistrationDialogStates.reg_info
    ),
    Window(
        Const(textblock["request_info"]["title"]),
        Button(Const(textblock["request_info"]["next"]), id="fio_next", on_click=fio_next),
        Button(Const(textblock["request_info"]["cancel"]), id="fio_cancel", on_click=fio_cancel),
        state=RegistrationDialogStates.fio
    ),
    Window(
        Const(textblock["input_surname"]["title"]),
        TextInput(id="surname_input", on_success=on_surname_entered),
        state=RegistrationDialogStates.surname
    ),
    Window(
        Const(textblock["input_name"]["title"]),
        TextInput(id="name_input", on_success=on_name_entered),
        state=RegistrationDialogStates.name
    ),
    Window(
        Const(textblock["input_patronymic"]["title"]),
        TextInput(id="patronymic_input", on_success=on_patronymic_entered),
        state=RegistrationDialogStates.patronymic
    ),
    Window(
        Const(textblock["confirm"]["title"]),
        Button(Const(textblock["confirm"]["confirm_and_send"]), id="confirm_data_send", on_click=confirm_data_send),
        Button(Const(textblock["confirm"]["change"]), id="confirm_data_change", on_click=confirm_data_change),
        Button(Const(textblock["confirm"]["cancel"]), id="confirm_data_cancel", on_click=confirm_data_cancel),
        state=RegistrationDialogStates.confirm_data,
    ),
)

registration_router.include_router(registration_dialog)