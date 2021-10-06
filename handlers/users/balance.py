from aiogram.dispatcher import FSMContext

from loader import dp
from states.UserState import Form
from utils.db_api import users_db
from aiogram import types

@dp.message_handler(text="Balance", state=Form.GetInfo)
async def check(msg: types.Message, state: FSMContext):
    balance = users_db.find_one({'user_id': msg.chat.id})
    await msg.answer("Your balance: \n\n💰 {} coin".format(balance['coin']))
