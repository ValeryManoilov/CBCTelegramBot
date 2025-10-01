from aiogram.fsm.state import State, StatesGroup

class MainMenuDialogStates(StatesGroup):
    main_menu = State()
    support = State()

class RegistrationDialogStates(StatesGroup):
    reg_info = State()
    fio = State()
    confirm_data = State()
    surname = State()
    name = State()
    patronymic = State()