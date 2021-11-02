from aiogram.utils.callback_data import CallbackData

comment_callback = CallbackData("comment", "item_name")
like_callback = CallbackData("like", "item_name")
buy_callback = CallbackData("coin", "quantity")