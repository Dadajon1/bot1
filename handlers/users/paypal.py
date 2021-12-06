from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from data import config
from keyboards.inline.payment import buy_coins
from loader import dp
from states.UserState import Form

import paypalrestsdk
import logging

paypalrestsdk.configure({
  "mode": "sandbox", # sandbox or live
  "client_id": config.PAYPAL_CLIENT_ID,
  "client_secret": config.PAYPAL_CLIENT_SECRET})

@dp.message_handler(text="Buy Coins", state="*")
async def send_coins_button(msg: types.Message):
    await msg.answer(text="How many coins do you want to buy?"
                    "\n\nOnce you pay online, you'll have coins to submit new orders."
                    "\n\nPlease select from bellow options:", reply_markup=buy_coins)

    await Form.PayQuery.set()

@dp.callback_query_handler(text_contains="coin", state=Form.PayQuery)
async def get_coins(call: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        num = 0
        coins = 0
        if call.data == 'coin:5':
            num += 5
            coins += 80
        if call.data == 'coin:10':
            num += 10
            coins += 165
        if call.data == 'coin:15':
            num += 15
            coins += 255
        if call.data == 'coin:20':
            num += 20
            coins += 350
        data['num'] = num * 1.1
        data['coins'] = coins
        # await call.message.answer(text=num)
        text = f"You want to add {coins} coins to your account. You will have to pay ${num} USD and you will also pay a 10% service fee. Your total payment invoice is ${num}.5 USD.\n\n"
        text += "Which payment gateway would you like to use?\n"
        text += "Please select one of the payment options bellow, to complete your purchase."
        payment = paypalrestsdk.Payment({
            "intent": "sale",
            "payer": {
                "payment_method": "paypal"},
            "redirect_urls": {
                "return_url": "https://t.me/instaengagement_bot",
                "cancel_url": "https://t.me/instaengagement_bot"},
            "transactions": [{
                "item_list": {
                    "items": [{
                        "name": "item",
                        "sku": "item",
                        "price": num,
                        "currency": "USD",
                        "quantity": 1}]},
                "amount": {
                    "total": num,
                    "currency": "USD"},
                "description": "This is the payment transaction description."}]})

        if payment.create():
            print("Payment created successfully")
        else:
            print(payment.error)

        for link in payment.links:
            if link.rel == "approval_url":
                approval_url = str(link.href)
                id = approval_url.split('=')[-1]
                print("Redirect for approval: %s" % (id))

                payment_key = InlineKeyboardMarkup(inline_keyboard=[
                    [
                        InlineKeyboardButton(text="Payment", url=f'https://www.paypal.com/checkoutnow?token={id}')
                    ]
                ])
                await call.message.edit_text(text, reply_markup=payment_key)







