from keyboards.inline.payment import comment_key, like_key
from loader import dp, bot
from aiogram import types
from utils.db_api import users_db
from states.UserState import Form


@dp.message_handler(text="Receive Comment", state=Form.GetInfo)
async def receive_like(msg: types.Message):
    balance = users_db.find_one({'user_id': msg.chat.id})

    text = f"❇️ Receive Comments 💬\n" \
           f"------------------------------\n" \
           f"💰Your Balance: {balance['coin']}\n" \
           f"📈: How many comments do you want⁉\n️"
    await msg.reply(text=text, reply_markup=comment_key)


@dp.message_handler(text="Receive Like", state=Form.GetInfo)
async def receive_comment(msg: types.Message):
    balance = users_db.find_one({'user_id': msg.chat.id})
    text = f"❇️ Receive Like ❤️\n" \
           f"------------------------------\n" \
           f"💰Your Balance: {balance['coin']}\n" \
           f"📈: How many comments do you want⁉️\n"
    await msg.reply(text=text, reply_markup=like_key)