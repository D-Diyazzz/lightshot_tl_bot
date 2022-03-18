from pickle import NONE
import parser_lightshot

import logging
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5175697170:AAE-3h-OGTtTujWNt8OjFCr1XsAXuIR8Ja4'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token = API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["/run", "/help"]
    keyboard.add(*buttons)
    
    await message.answer("Привет\nЯ парсер сайта LightShot🪶\nНапиши /run что бы получить рандомный скриншот", reply_markup=keyboard)
    


@dp.message_handler(commands=['run'])
async def send_img(message: types.Message):
    image = parser_lightshot.rand_hashcode()
    try:
        await message.answer("Вот твой скриншот🖼\n\n"+image)
    except TypeError:
        await message.answer("Вот твой скриншот🖼\n\n"+parser_lightshot.rand_hashcode())


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)