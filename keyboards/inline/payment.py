from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from keyboards.inline.callback_data import comment_callback, buy_callback

payment_key = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Payment", url="https://www.paypal.com/uz/home")
    ]
])

comment_key = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="5 Comments", callback_data="comment:comment5"),
            InlineKeyboardButton(text="10 Comments", callback_data="comment:comment10"),
        ],
        [
            InlineKeyboardButton(text="15 Comments", callback_data="comment:comment15"),
            InlineKeyboardButton(text="20 Comments", callback_data="comment:comment20"),
        ],[
            InlineKeyboardButton(text="30 Comments", callback_data="comment:comment30"),
            InlineKeyboardButton(text="50 Comments", callback_data="comment:comment50"),
        ]
    ]
)

# comment_key = InlineKeyboardMarkup(row_width=2)
# comment_key.insert(InlineKeyboardButton(text="5 Comments", callback_data=comment_callback.new(item_name='comment5')))
# comment_key.insert(InlineKeyboardButton(text="10 Comments", callback_data=comment_callback.new(item_name='comment10')))
# comment_key.insert(InlineKeyboardButton(text="15 Comments", callback_data=comment_callback.new(item_name='comment15')))
# comment_key.insert(InlineKeyboardButton(text="20 Comments", callback_data=comment_callback.new(item_name='comment20')))
#

like_key = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="5 Like", callback_data="like:like5"),
            InlineKeyboardButton(text="10 Like", callback_data="like:like10"),
        ],
        [
            InlineKeyboardButton(text="15 Like", callback_data="like:like15"),
            InlineKeyboardButton(text="20 Like", callback_data="like:like20"),
        ],
        [
            InlineKeyboardButton(text="30 Like", callback_data="like:like30"),
            InlineKeyboardButton(text="50 Like", callback_data="like:like50"),
        ]
    ]
)

invite_friends = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Share Friends", switch_inline_query_current_chat='')
        ]
    ]
)

buy_coins = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="80 💰 = $5", callback_data=buy_callback.new(5)),
            InlineKeyboardButton(text="165 💰 = $10", callback_data=buy_callback.new(10)),
        ],
        [
            InlineKeyboardButton(text="255 💰 = $15", callback_data=buy_callback.new(15)),
            InlineKeyboardButton(text="350 💰 = $20", callback_data=buy_callback.new(20)),
        ]
    ],
)