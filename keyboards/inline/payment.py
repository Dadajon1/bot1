from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from keyboards.inline.callback_data import comment_callback

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