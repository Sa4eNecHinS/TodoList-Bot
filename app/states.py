from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext


class Tasks(StatesGroup):
    task = State()
    #  priority = State()
