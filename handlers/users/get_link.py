from keyboards.inline import payment_key
from loader import dp
from aiogram import types
from aiogram.types.inline_keyboard import InlineKeyboardMarkup, InlineKeyboardButton

from states.UserState import Form


@dp.message_handler(text="Add post", state=Form.GetInfo)
async def get_link(msg: types.Message):
    text = "You must pay first to post.\n" \
           "Click the button below to pay."
    await msg.answer(text=text, reply_markup=payment_key)
