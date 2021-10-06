from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

payment_key = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Payment", url="https://www.paypal.com/uz/home")
    ]
])

comment_key = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="5 Comments", callback_data="comment5"),
            InlineKeyboardButton(text="10 Comments", callback_data="comment10"),
        ],
        [
            InlineKeyboardButton(text="15 Comments", callback_data="comment15"),
            InlineKeyboardButton(text="20 Comments", callback_data="comment20"),
        ]
    ]
)


like_key = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="5 Like", callback_data="like5"),
            InlineKeyboardButton(text="10 Like", callback_data="like10"),
        ],
        [
            InlineKeyboardButton(text="15 Like", callback_data="like15"),
            InlineKeyboardButton(text="20 Like", callback_data="like20"),
        ]
    ]
)