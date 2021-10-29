from keyboards.default import main_menu
from loader import dp
from aiogram import types

from states.UserState import Form

@dp.message_handler(text='Service Policy', state="*")
async def privacy_policy(msg: types.Message):
    await msg.answer(
        text="""<b>👑 📜 Rules 📜 👑
1️⃣ Do not attempt to cheat.
------------------------------
2️⃣ You have to write your own comments.
------------------------------
3️⃣ Do not write negative comments about yourself. (Be kind to yourself 😌)
------------------------------
4️⃣ Do not write exaggerated positive comments about yourself either (we know it is tempting 😉 )
------------------------------
5️⃣ Do not get comments on the behalf of anyone. Invite them to join instead.
------------------------------
6️⃣ Use the same account to give and receive comments. (We don’t care if you’re famous, or else you wouldn’t be here).
------------------------------
7️⃣ If you share a link from a different Instagram account than the one you registered with, we will take 25 coins from you...
------------------------------
8️⃣ Read those 7 rules again, we are very serious. We will ban you if you break them.
------------------------------</b>""",
        reply_markup=main_menu)
