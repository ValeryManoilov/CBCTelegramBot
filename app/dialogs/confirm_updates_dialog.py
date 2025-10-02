from aiogram_dialog import Window, Dialog
from aiogram_dialog.widgets.input import TextInput
from aiogram_dialog.widgets.text import Const
from aiogram import Router
from app.states import UpdateUserdataStates
from app.dialog_functions import (
    update_on_surname_entered, update_on_name_entered, update_on_patronymic_entered
)
import json

with open("app/texts.json", 'r', encoding='utf-8') as file:
    textblock = json.load(file)["confirm_updates_dialog"]

confirm_updates_router = Router()

confirm_updates_dialog = Dialog(
    Window(
        Const(textblock["input_new_surname"]["title"]),
        TextInput(id="update_surname_input", on_success=update_on_surname_entered),
        state=UpdateUserdataStates.surname
    ),
    Window(
        Const(textblock["input_new_name"]["title"]),
        TextInput(id="update_name_input", on_success=update_on_name_entered),
        state=UpdateUserdataStates.name
    ),
    Window(
        Const(textblock["input_new_patronymic"]["title"]),
        TextInput(id="update_patronymic_input", on_success=update_on_patronymic_entered),
        state=UpdateUserdataStates.patronymic
    ),
)

confirm_updates_router.include_router(confirm_updates_dialog)