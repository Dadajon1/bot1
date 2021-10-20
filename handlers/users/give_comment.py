import random

import instaloader
from aiogram import types
from bs4 import BeautifulSoup
from selenium import webdriver
from aiogram.dispatcher import FSMContext

from loader import dp
from states.UserState import Form
from utils.db_api import users_db, like_link_db, comment_link_db
from keyboards.default.send_link import check_list, main_menu, okay_skip



@dp.message_handler(text="Give Comment", state=Form.GetInfo)
async def send_link_message(msg: types.Message):
    await msg.answer("Please send your username.")
    await Form.GiveComment.set()

@dp.message_handler(state=Form.GiveComment)
async def get_user(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        username = msg.text
        print(username)
        users_db.find_and_modify({'user_id': msg.chat.id}, {'$set': {'insta_username': username}}, upsert=False,
                                 full_response=True)
        telegram_id = []
        for i in comment_link_db.find():
            print(i)
            if msg.chat.id != i['user_id'] and i['count'] > 0:
                telegram_id = i['view_list']
                print(telegram_id)
                if msg.chat.id in telegram_id:
                    print(msg.chat.id in telegram_id)
                    continue
                link = i['link']
                comment = i['comment']
                post_username = i['username']
                i['count'] -= 1
                telegram_id.append(msg.chat.id)
                comment_link_db.find_and_modify({'user_id': i['user_id']}, {'$set': {'view_list': telegram_id}}, upsert=False, full_response=True)
                data["link"] = link
                data["comment"] = comment
                data["post_username"] = username
                data['user'] = post_username
                print(data)
                break
        try:
            print(data)
            text = "❇️ Post by @{} ❇ \n️".format(post_username)
            text += "------------------------------\n"
            text += "📎 {}\n".format(link)
            text += "------------------------------\n"
            text += "📝 I will send you a comment 📝\n"
            text += "🧠 Use your account {} 🧠\n".format(username)
            text += "🔖 Copy the comment and paste it on the post 🔖\n"
            text += "------------------------------\n"
            text += "👍 Click “okay” for me to send the comment or click ❌ Skip if you want a different link.\n"
            await msg.answer(text=text, reply_markup=okay_skip)
            await Form.SendComment.set()
        except:
            text = "Hozircha linklar yo'q"
            await msg.answer(text=text)
            await Form.GetInfo.set()


@dp.message_handler(state=Form.SendComment, text="Okay")
async def send_comment(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        await msg.answer("Note: Please copy the text below, then open the post link and send the copied text as a comment for this post.")
        await msg.answer(text=f"{random.choice(data['comment'])}")
        await msg.answer("Press the `I'm Done` button after you did it.\n⚠️ Limitation: You have only 5 minutes to finish this comment. Otherwise it will be given to someone else!", reply_markup=check_list)
        await Form.CheckComment.set()

@dp.message_handler(state=Form.CheckComment, text="I'm Done")
async def check_user(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        username = data["post_username"]
        print(data)
        await msg.answer("The verification process may take some time. Please wait.")
        L = instaloader.Instaloader()
        L.load_session_from_file('bexruz.nutfilloyev',
                                 '/Users/yoshlikmedia/Projects/Navbatchilik-bot/handlers/users/instaloader.session')

        driver = webdriver.Chrome('/Users/yoshlikmedia/Projects/Navbatchilik-bot/chromedriver')
        link = data['link']
        user = data['user']
        driver.get(link)

        soup = BeautifulSoup(driver.page_source, 'html.parser')

        img = soup.find('img', class_='FFVAD')
        img_url = img['src']
        print(img_url)

        profile = instaloader.Profile.from_username(L.context, user)
        print(profile.get_posts())

        for post in profile.get_posts():
            # like_list = []
            comment_list = []
            print(post.url)
            if post.url[:160] == img_url[:160]:
                # post_likes = post.get_likes()
                post_comments = post.get_comments()

                # for likee in post_likes:
                #     like_list.append(likee.username)

                for comment in post_comments:
                    # print(comment.owner.username)
                    comment_list.append(comment.owner.username)
                print("=" * 100)
                break

        if username in comment_list:
            send_text = "Comment ✅\n\n"
        else:
            send_text = "Comment ❌\n\n"

        if username in comment_list:
            coin = users_db.find_one()
            coin = coin['coin']
            coin += 10
            users_db.find_and_modify({'user_id': msg.chat.id}, {'$set': {'coin': coin}}, upsert=False,
                                     full_response=True)
            send_text += "coin: {}\n".format(coin)
        else:
            send_text += "Please fulfill condition.\n"

        await msg.answer(send_text, reply_markup=main_menu)
        await Form.GetInfo.set()
