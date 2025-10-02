
from aiogram_dialog import Window, Dialog
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.input import TextInput
from aiogram_dialog.widgets.text import Const
from aiogram import Router
from app.states import RegistrationDialogStates
from app.dialog_functions import (
    reg_info_next, reg_info_cancel, fio_next, fio_cancel,
    confirm_data_send, confirm_data_change, confirm_data_cancel,
    on_surname_entered, on_name_entered, on_patronymic_entered,
)

registration_router = Router()

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
        Const("Введите фамилию: "),
        TextInput(id="surname_input", on_success=on_surname_entered),
        state=RegistrationDialogStates.surname
    ),
    Window(
        Const("Введите имя: "),
        TextInput(id="name_input", on_success=on_name_entered),
        state=RegistrationDialogStates.name
    ),
    Window(
        Const("Введите отчество: "),
        TextInput(id="patronymic_input", on_success=on_patronymic_entered),
        state=RegistrationDialogStates.patronymic
    ),
    Window(
        Const("Подтверждение"),
        Button(Const("Подтвердить и отправить"), id="confirm_data_send", on_click=confirm_data_send),
        Button(Const("Изменить"), id="confirm_data_change", on_click=confirm_data_change),
        Button(Const("Отмена"), id="confirm_data_cancel", on_click=confirm_data_cancel),
        state=RegistrationDialogStates.confirm_data
    ),
)

registration_router.include_router(registration_dialog)