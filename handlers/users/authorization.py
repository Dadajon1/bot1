from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.default import main_menu
from states.UserState import Form
from loader import dp, bot
from datetime import datetime

from utils.db_api import users_db


@dp.message_handler(content_types='contact', state=Form.GetPhone)
async def contact_hand(message: types.Message, state: FSMContext):
    textback = ""
    async with state.proxy() as data:
        data['phone'] = str(message.contact.phone_number).replace('+', '').replace(' ', '')
        req_db = users_db.update_one({'phone': data['phone']}, {'$set': {
            "phone": data['phone'],
            "updated": datetime.now(),
            "user_id": message.from_user.id,
            "user_info": message.from_user.full_name,
            "username": message.from_user.username,
            }
        }, upsert=True)
        if (req_db.matched_count):
            textback = "I'm glad to see you again, {}".format(message.from_user.first_name)

        else:
            textback = "Welcome {}".format(message.from_user.first_name)
        print(textback)
    await message.answer(textback, reply_markup=main_menu)
    await Form.GetInfo.set()
