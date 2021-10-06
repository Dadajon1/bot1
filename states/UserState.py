from aiogram.dispatcher.filters.state import StatesGroup, State

class Form(StatesGroup):
    GetPhone = State()
    GetInfo = State()
    GiveLike = State()
    CheckLike = State()
    GiveComment = State()
    CheckComment = State()
    GetLink = State()
