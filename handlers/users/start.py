from datetime import datetime

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.utils.deep_linking import decode_payload

from keyboards.default import send_phone, main_menu
from aiogram.dispatcher import FSMContext
from states.UserState import Form
from loader import dp, bot
from utils.db_api import users_db

# Start State
@dp.message_handler(CommandStart(), state='*')
async def bot_start(message: types.Message, state: FSMContext):
    textback = ""
    args = message.get_args()
    async with state.proxy() as data:
        req_db = users_db.update_one({'user_id': message.from_user.id},
            {'$set': {
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
            balance = users_db.find_and_modify({'user_id': message.chat.id}, {'$set': {"coin": 10}}, upsert=False)
        print(textback)
    try:
        await bot.send_message(args, "Your friend has joined")
        req_db = users_db.find_one({'user_id': args})
        coin = req_db['coin']
        coin += 10
        users_db.update_one({'user_id': args}, {'$set': {'coin': coin}}, upsert=True)
        await bot.send_message(args, "Your balance: {}".format(coin))
    except:
        await message.answer(textback, reply_markup=main_menu)
        await Form.GetInfo.set()

