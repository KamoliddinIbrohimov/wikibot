import asyncio
import logging
import wikipedia

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

API_TOKEN = '5068096391:AAGv_x0t32OND988mCnK_lAwcgH_T78xZec'

# Configure logging
logging.basicConfig(level=logging.INFO)


# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)



#defould keyboard
languageButton = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🇺🇿Uzbek"),
            KeyboardButton(text="🇷🇺Русский"),
        ],
        [
            KeyboardButton(text="🇺🇸English"),
        ],
    ],
    resize_keyboard=True
)

backButton = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🔙")
        ],
    ],
    resize_keyboard=True
)

#command /start
@dp.message_handler(commands='start')
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` command
    """
    await message.delete()
    await message.answer("Wikipeida Botiga Xush Kelibsiz!🇺🇿\n"
                        "Добро пожаловать в бот Википедии!🇷🇺\n"
                        "Welcome to the Wikipedia Bot!🇺🇸\n", reply_markup=languageButton)


#command /help
@dp.message_handler(commands="help")
async def help_com(message: types.Message):
    """
    This handler will be called when user sends `/help` command
    """
    await message.answer("Assalomu alekum Wikipedia botimizga hush kelibsiz.\n"
                         "Botdan foydalanish uchun so'z kiriting🇺🇿\n"
                         "Здравствуйте и добро пожаловать в наш бот из Википедии.\n"
                         "Введите пароль для использования бота🇷🇺\n"
                         "Hello and welcome to our Wikipedia bot.\n"
                         "Enter password to use bot🇺🇸\n"
                         "🔰🔰🔰🔰🔰🔰🔰🔰🔰🔰🔰🔰🔰🔰🔰🔰🔰🔰🔰\n"
                         "/start - Boshlash/Начинать/Start🏁\n"
                         "/help - Yordam/Помощь/Help🦸‍♂️")

@dp.message_handler(text="🇺🇿Uzbek")
async def uz_lan(message: types.Message):
    await message.answer("🇺🇿Uzbek.\n"
                         "So'z kiriting✏️", reply_markup=backButton)
    await message.delete()
    wikipedia.set_lang('uz')


@dp.message_handler(text="🇷🇺Русский")
async def uz_lan(message: types.Message):
    await message.answer("🇷🇺Русский.\n"
                         "Введите слово✏", reply_markup=backButton)
    await message.delete()
    wikipedia.set_lang('ru')


@dp.message_handler(text="🇺🇸English")
async def uz_lan(message: types.Message):
    await message.answer("🇺🇸English.\n"
                         "Enter a word✏", reply_markup=backButton)
    await message.delete()
    wikipedia.set_lang('en')



@dp.message_handler(text="🔙")
async def beck(message: types.Message):
    await message.answer("Tilni tanlang🇺🇿\n"
                         "Выберите язык🇷🇺\n"
                         "Select a language🇺🇸", reply_markup=languageButton)
    await message.delete()

@dp.message_handler()
async def sendWiki(message: types.Message):
    msg2 = await message.reply("🔍")
    try:
        print(message)
        response = wikipedia.summary(message.text)
        await message.answer(response, reply_markup=backButton)
        await msg2.delete()
    except:
        await msg2.delete()
        msg = await message.reply("Ushbu mavzu uchun maqola topilmadi🇺🇿\n"
                             "Не найдена статья по этой теме🇷🇺\n"
                             "No article found for this topic🇺🇸")
        msg1 = await message.reply("😞", reply_markup=backButton)
        await asyncio.sleep(8)
        await msg.reply_to_message.delete()
        await msg.delete()
        await msg1.delete()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
