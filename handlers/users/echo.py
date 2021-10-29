import instaloader
from aiogram import types
from bs4 import BeautifulSoup
from selenium import webdriver
from aiogram.dispatcher import FSMContext

from loader import dp
from states.UserState import Form
from utils.db_api import users_db, like_link_db, comment_link_db
from keyboards.default.send_link import check_list, main_menu, okay_skip



@dp.message_handler(text="Give Like", state="*")
async def send_link_message(message: types.Message, state: FSMContext):
    text = "Follow the link below and write Comment📃️\n"
    text += "Please do not try to cheat, everything will be checked.\n\n"
    text += "Link: https://www.instagram.com/p/COeT77ytHqY/\n"
    text += "Press the button to check."
    await message.answer(text=text, reply_markup=check_list)
    await Form.GiveComment.set()


@dp.message_handler(text="Check✅", state=Form.GiveComment)
async def get_user(msg: types.Message, state: FSMContext):
    await msg.answer("Please send your username. Without errors and flaws otherwise we will not be able to check you.")
    await Form.CheckComment.set()


@dp.message_handler(state=Form.CheckComment)
async def check_user(msg: types.Message, state: FSMContext):
    username = msg.text
    await msg.answer("The verification process may take some time. Please wait.")
    L = instaloader.Instaloader()
    L.load_session_from_file('bexruz.nutfilloyev',
                             '/Users/yoshlikmedia/Projects/Navbatchilik-bot/handlers/users/instaloader.session')
    driver = webdriver.Chrome('/Users/yoshlikmedia/Projects/Navbatchilik-bot/chromedriver')
    link = "https://www.instagram.com/p/COeT77ytHqY/"
    user = 'yoshlik_media'
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
        users_db.find_and_modify({'user_id': msg.chat.id}, {'$set': {'coin': coin}}, upsert=False, full_response=True)
        send_text += "coin: {}\n".format(coin)
    else:
        send_text += "Please fulfill condition.\n"

    await msg.answer(send_text, reply_markup=main_menu)
    await Form.GetInfo.set()
