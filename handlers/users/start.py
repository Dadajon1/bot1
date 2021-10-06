from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default import send_phone
from aiogram.dispatcher import FSMContext
from states.UserState import Form
from loader import dp


@dp.message_handler(CommandStart(), state='*')
async def bot_start(message: types.Message, state: FSMContext):
    await Form.GetPhone.set()
    text = f"Hi, <b>{message.from_user.full_name}!</b>\n"
    text += "Welcome to our bot.\n\n" \
            "Click the Send Number button to use the bot."
    await message.answer(text=text, reply_markup=send_phone)
