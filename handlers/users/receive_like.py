from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
from keyboards.default import main_menu
from keyboards.inline.payment import like_key
from loader import dp
from aiogram import types
from utils.db_api import users_db, like_link_db
from states.UserState import Form


@dp.message_handler(text="Receive Like", state="*")
async def receive_like(msg: types.Message):
    try:
        balance = users_db.find_one({'user_id': msg.chat.id})
        print("---", balance['coin'])
    except:
        balance = users_db.find_and_modify({'user_id': msg.chat.id}, {'$set': {"coin": 10}}, upsert=False)
        print("---", balance)
        balance = users_db.find_one({'user_id': msg.chat.id})
    text = f"❇️ Receive Like ❤️\n" \
           f"------------------------------\n" \
           f"💰Your Balance: {balance['coin']}\n" \
           f"------------------------------\n" \
           f"📈: How many likes do you want⁉️\n️"
    await msg.reply(text=text, reply_markup=like_key)
    await Form.RecieveLike.set()


@dp.callback_query_handler(text_contains="like", state=Form.RecieveLike)
async def get_comment(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        num = 0
        if call.data == 'like:like5':
            num += 5
        if call.data == 'like:like10':
            num += 10
        if call.data == 'like:like15':
            num += 15
        if call.data == 'like:like20':
            num += 20
        if call.data == 'like:like30':
            num += 30
        if call.data == 'like:like50':
            num += 50
        data['num'] = num

        await call.answer(cache_time=60)
        user_info = users_db.find_one({'user_id': call.message.chat.id})
        print(user_info)
        if 'insta_username' not in user_info.keys():
            print("1")
            await call.message.answer(text="Please send your username without @")
            await Form.AddUsernameLike.set()
        else:
            data['username'] = user_info['insta_username']
            text = f"❇️ Your Link ❇️ \n" \
                   f"------------------------------ \n" \
                   f"👤 The post must be for the <code>{user_info['insta_username']}</code>\n" \
                   f"🛒 Amount: {num}\n" \
                   f"⚠️ Remove UTM source codes (Learn)\n" \
                   f"------------------------------\n" \
                   f"📎 Send me the link to your post ⬇️"
            await call.message.answer(text=text)
            await Form.GetLikeLink.set()


@dp.message_handler(state=Form.AddUsernameLike)
async def add_username(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        username = msg.text
        print(data)
        data['username'] = username
        users_db.find_and_modify({'user_id': msg.chat.id}, {'$set': {'insta_username': username}}, upsert=False,
                                 full_response=True)
        like_link_db.find_and_modify({'user_id': msg.chat.id}, {'$set': {'username': username}}, upsert=False,
                                     full_response=True)

        user_info = users_db.find_one({'user_id': msg.chat.id})
        text = f"❇️ Your Link ❇️ \n" \
               f"------------------------------ \n" \
               f"👤 The post must be for the <code>{user_info['insta_username']}</code>\n" \
               f"🛒 Amount: {data['num']}\n" \
               f"⚠️ Remove UTM source codes (Learn)\n" \
               f"------------------------------\n" \
               f"📎 Send me the link to your post ⬇️"
        await msg.answer(text=text)
        await Form.GetLikeLink.set()


@dp.message_handler(state=Form.GetLikeLink)
async def get_comment_link(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['link'] = msg.text
        print(data)
        text = f"Like\n\n" \
               f"Amount {data['num']}\n" \
               f"Link: {msg.text}\n\n"
        like_link_db.update_one({'user_id': msg.from_user.id},
                                {'$set': {
                                    "link": data['link'],
                                    "count": data['num'],
                                    "username": data['username'],
                                    "is_like": True,
                                    "view_list": [msg.chat.id],
                                        }
                                    }, upsert=True)
        coin = users_db.find_one()
        coin = coin['coin']
        coin -= data['num']
        await msg.reply(text=text)
        await msg.answer("Like Accepted", reply_markup=main_menu)
        await Form.GetInfo.set()
