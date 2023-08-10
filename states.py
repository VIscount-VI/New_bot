from aiogram.dispatcher.filters.state import State, StatesGroup
class FeedbState(StatesGroup):
    body = State()