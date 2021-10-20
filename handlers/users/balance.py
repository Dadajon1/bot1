from aiogram.dispatcher import FSMContext

from loader import dp
from states.UserState import Form
from utils.db_api import users_db
from aiogram import types


@dp.message_handler(text="My Profile", state=Form.GetInfo)
async def check(msg: types.Message):
    balance = users_db.find_one({'user_id': msg.chat.id})
    text = "❇️ My Profile ❇\n️"
    text += "–"*20
    text += f"\n🆔 {balance['user_id']}\n"
    text += f"👤 {balance['user_id']} (Telegram ID)\n"
    text += "–"*20
    try:
        text += "\n💰Your balance: {} coin\n".format(balance['coin'])
    except Exception as ex:
        print(ex)
    text += "–" * 20
    try:
        text += f"\n👤 @<code>{balance['insta_username']}</code>"
    except Exception as ex:
        print(ex)

    await msg.answer(text=text)
