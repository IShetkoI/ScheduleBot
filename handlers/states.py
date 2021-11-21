from aiogram.dispatcher.filters.state import StatesGroup, State


class States(StatesGroup):
    new = State()
    edit = State()
