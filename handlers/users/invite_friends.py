from loader import dp
from aiogram import types

from states.UserState import Form


@dp.message_handler(text='Invite Friends', state="*")
async def invite_link(msg: types.Message):
    USER_ID = msg.chat.id
    text = f"""โ๏ธ Invite Friend  โ๏ธ
------------------------------
๐ You are the best friend anyone can wish for.
------------------------------
Send this link to your friend โคต๏ธ
๐ t.me/instaengagement_bot?start={USER_ID}"""
    await msg.reply(text=text)