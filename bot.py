from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

from config import *
from db import *
from sub import *
from qr import make_qr
from affiliate import handle_ref
from backup import create_backup

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

init()

@dp.message_handler(commands=['start'])
async def start(m: types.Message):
    user = str(m.from_user.id)
    ref = m.get_args()

    handle_ref(user, ref)

    kb = types.InlineKeyboardMarkup()
    kb.add(types.InlineKeyboardButton("💰 خرید", callback_data="buy"))
    kb.add(types.InlineKeyboardButton("💸 کیف پول", callback_data="wallet"))
    kb.add(types.InlineKeyboardButton("👥 دعوت", callback_data="ref"))

    kb.add(types.InlineKeyboardButton("💾 بکاپ", callback_data="backup"))

    await m.answer("⚡ Berserk VPN", reply_markup=kb)

@dp.callback_query_handler(lambda c: c.data == "buy")
async def buy(c: types.CallbackQuery):
    user = str(c.from_user.id)

    sub = get_free_sub()
    if not sub:
        return await c.message.answer("❌ موجودی تمام شد")

    sub_id, link = sub
    assign_sub(sub_id, user)

    qr = make_qr(link, user)

    await c.message.answer_photo(open(qr, "rb"), caption=f"✅ فعال شد\n{link}")

@dp.callback_query_handler(lambda c: c.data == "wallet")
async def wallet(c: types.CallbackQuery):
    await c.message.answer("💸 کیف پول فعلاً ساده است")

@dp.callback_query_handler(lambda c: c.data == "ref")
async def ref(c: types.CallbackQuery):
    user = str(c.from_user.id)
    code = user[-5:]
    link = f"https://t.me/YOUR_BOT?start={code}"
    await c.message.answer(f"👥 لینک دعوت:\n{link}")

@dp.callback_query_handler(lambda c: c.data == "backup")
async def backup(c: types.CallbackQuery):
    if c.from_user.id != ADMIN_ID:
        return await c.message.answer("⛔ دسترسی ندارید")

    file = create_backup()

    await c.message.answer_document(
        types.InputFile(file),
        caption="💾 بکاپ دیتابیس آماده شد"
    )

executor.start_polling(dp)
