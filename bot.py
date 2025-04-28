import os
import logging
import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart
from aiogram.types import FSInputFile, InlineKeyboardMarkup, InlineKeyboardButton

# Ваш токен
TOKEN = os.getenv('BOT_TOKEN')
# Ваш Telegram ID
MY_TELEGRAM_ID = 1736108313

# Инициализация бота и диспетчера
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Клавиатура
keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="📚 Programs & Pricing", callback_data="programs")],
    [InlineKeyboardButton(text="📞 Book a Call", callback_data="book_call")],
    [InlineKeyboardButton(text="💳 Payment", url="https://google.com")],
    [InlineKeyboardButton(text="❓ FAQ", callback_data="faq")],
    [InlineKeyboardButton(text="🛟 Support", callback_data="support")]
])

# Стартовое сообщение
@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer(
        "Welcome to LuxService Assistant!\n\n"
        "This bot was created as part of a portfolio project.\n"
        "Developer: Albina\n\n"
        "✨ Everything for your comfort, growth, and success.\n\n"
        "Please choose an option below:",
        reply_markup=keyboard
    )

# Обработка нажатий на кнопки
@dp.callback_query(F.data == "programs")
async def send_programs(callback: types.CallbackQuery):
    image = FSInputFile("price_image.jpg")  # Убедись, что картинка лежит рядом с файлом
    await callback.message.answer_photo(image, caption="Here are our Programs and Pricing!")

@dp.callback_query(F.data == "book_call")
async def book_call(callback: types.CallbackQuery):
    await callback.message.answer(
        "Please provide your information:\n\n"
        "1. Your Name\n"
        "2. Email Address\n"
        "3. Preferred Contact Method (Telegram / WhatsApp / Phone)\n"
        "4. Preferred Date and Time\n\n"
        "Our manager will contact you shortly after!"
    )

@dp.callback_query(F.data == "faq")
async def faq(callback: types.CallbackQuery):
    await callback.message.answer(
        "Frequently Asked Questions:\n\n"
        "❓ How to book a consultation?\n"
        "👉 Click 'Book a Call' and fill the form.\n\n"
        "❓ How can I pay?\n"
        "👉 Click 'Payment' to proceed with secure payment.\n\n"
        "❓ Can I get a refund?\n"
        "👉 Please contact Support for refund policy details."
    )

@dp.callback_query(F.data == "support")
async def support(callback: types.CallbackQuery):
    await callback.message.answer(
        "🛟 For any support issues, please contact our manager:\n"
        "@your_support_contact\n\n"
        "We are here to help you 24/7!"
    )

# Основной запуск
async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())