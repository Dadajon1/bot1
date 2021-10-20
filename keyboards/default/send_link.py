from aiogram.types.reply_keyboard import ReplyKeyboardMarkup, KeyboardButton

send_phone = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Send Number", request_contact=True)
        ]
    ],
    one_time_keyboard=True,
    resize_keyboard=True,
)

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Give Like"),
            KeyboardButton(text="Receive Like")
        ],
        [
            KeyboardButton(text="Give Comment"),
            KeyboardButton(text="Receive Comment")
        ],
        [
            KeyboardButton(text="My Profile"),
            KeyboardButton(text="Invite Friends"),

        ],
        [
            KeyboardButton(text="Payment History"),
            KeyboardButton(text="Service Policy")
        ]
    ],
    resize_keyboard=True,
)

check_list = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="I'm Done")
        ]
    ],
    one_time_keyboard=True,
    resize_keyboard=True,
)

okay_skip = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Okay"),
            KeyboardButton(text="Skip")
        ]
    ],
    one_time_keyboard=True,
    resize_keyboard=True,
)

comment_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Accept')
        ]
    ],
    one_time_keyboard=True,
    resize_keyboard=True
)
