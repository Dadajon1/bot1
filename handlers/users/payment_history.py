from aiogram import types
from loader import dp
from states.UserState import Form


@dp.message_handler(text="Payment History", state="*")
async def payment_history(msg: types.Message):
    await msg.reply("Your payment history: \n\n"
                    "...")
