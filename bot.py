import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

from config import *
from db import *
from sub import *
from affiliate import reward_ref
from utils import make_qr

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

init()

@dp.message_handler(commands=['start'])
async def start(m: types.Message):
    kb = types.InlineKeyboardMarkup()

    kb.add(types.InlineKeyboardButton("💰 خرید", callback_data="buy"))
    kb.add(types.InlineKeyboardButton("💸 کیف پول", callback_data="wallet"))

    await m.answer("⚡ Berserk VPN Ready", reply_markup=kb)


@dp.callback_query_handler(lambda c: c.data == "buy")
async def buy(c: types.CallbackQuery):
    user = str(c.from_user.id)

    sub = get_sub()
    if not sub:
        return await c.message.answer("❌ No Sub Available")

    sub_id, link = sub[0], sub[1]

    assign_sub(sub_id, user)

    reward_ref(user)

    qr = make_qr(link, user)

    await c.message.answer_photo(open(qr, "rb"), caption=link)


@dp.callback_query_handler(lambda c: c.data == "wallet")
async def wallet(c: types.CallbackQuery):
    cur.execute("SELECT balance FROM users WHERE id=?", (str(c.from_user.id),))
    bal = cur.fetchone()

    await c.message.answer(f"💰 Balance: {bal[0] if bal else 0}")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)