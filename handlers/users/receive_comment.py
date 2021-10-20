from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
from keyboards.default import main_menu
from keyboards.default.send_link import comment_button
from keyboards.inline.payment import comment_key
from loader import dp, bot
from aiogram import types
from utils.db_api import users_db, comment_link_db
from states.UserState import Form


@dp.message_handler(text="Receive Comment", state=Form.GetInfo)
async def receive_like(msg: types.Message):
    balance = users_db.find_one({'user_id': msg.chat.id})
    try:
        text = f"❇️ Receive Comments 💬\n" \
               f"------------------------------\n" \
               f"💰Your Balance: {balance['coin']}\n" \
               f"📈: How many comments do you want⁉\n️"
        await msg.reply(text=text, reply_markup=comment_key)
        await Form.RecieveComment.set()
    except:
        await msg.reply("Sizda yetarli mablag' mavjud emas!")
        await Form.GetInfo.set()


@dp.callback_query_handler(text_contains="comment", state=Form.RecieveComment)
async def get_comment(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        num = 0
        if call.data == 'comment:comment5':
            num += 5
        if call.data == 'comment:comment10':
            num += 10
        if call.data == 'comment:comment15':
            num += 15
        if call.data == 'comment:comment20':
            num += 20
        balance = users_db.find_one({'user_id': call.message.chat.id})
        data['num'] = num


        await call.answer(cache_time=60)
        user_info = users_db.find_one({'user_id': call.message.chat.id})
        print(user_info)
        if 'insta_username' not in user_info.keys():
            print("1")
            await call.message.answer(text="Iltimos Instagram username yuboring")
            await Form.AddUsername.set()
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
            await Form.GetCommentLink.set()


@dp.message_handler(state=Form.AddUsername)
async def add_username(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        username = msg.text
        print(data)
        data['username'] = username
        users_db.find_and_modify({'user_id': msg.chat.id}, {'$set': {'insta_username': username}}, upsert=False,
                                 full_response=True)
        comment_link_db.find_and_modify({'user_id': msg.chat.id}, {'$set': {'username': username}}, upsert=False,
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
        await Form.GetCommentLink.set()


@dp.message_handler(state=Form.GetCommentLink)
async def get_comment_link(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['link'] = msg.text
        print(data)
        text = f"Comment\n\n" \
               f"Amount {data['num']}\n" \
               f"Link: {msg.text}\n\n" \
               f"-If this is correct please confirm, if not then please start over:"
        await msg.reply(text=text, reply_markup=comment_button)
        await Form.GetCommentText.set()


@dp.message_handler(state=Form.GetCommentText, text='Accept')
async def get_comment_text(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        text = """💬 Write Your Comments 💬
------------------------------
🧠 Use \ (backward slash) and a number to number the comments.
✳️ example (if I wanted 3 comments, here is how)
\1 You have a nice voice Beyonce
\2 I cannot wait for the new music to come out
\3 Can I get a free ticket to your concert?
            
👀 Double-check your comment’s spelling and grammar. Once you click the confirm button, you will not be able to make any more changes."""
        await msg.answer(text=text)
        await Form.SetCommentText.set()


@dp.message_handler(state=Form.SetCommentText)
async def set_comment_text(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comment'] = msg.text
        comment_link_db.update_one({'user_id': msg.from_user.id},
                           {'$set': {
                               "link": data['link'],
                               "comment": data['comment'].split('\n'),
                               "count": data['num'],
                               "username": data['username'],
                               "is_comment": True,
                               "view_list": [msg.chat.id],
                           }
                           }, upsert=True)


        await msg.answer("Qabul qilindi.", reply_markup=main_menu)
        await Form.GetInfo.set()
