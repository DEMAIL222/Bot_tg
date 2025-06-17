import logging
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters.command import Command
from transliterate import translit
import os

TOKEN = os.getenv('TOKEN')
bot = Bot(token=TOKEN)
dp = Dispatcher()
logging.basicConfig(level=logging.INFO)

@dp.message(Command(commands=['start']))
async def proccess_command_start(messege: Message):
    user_name = messege.from_user.full_name
    user_id = messege.from_user.id
    text = f'Привет, {user_name}, отправь мне ФИО!'
    logging.info(f'{user_name} {user_id} запустил бота')
    await bot.send_message(chat_id=user_id, text=text)

@dp.message()
async def send_translate(messege: Message):
    user_name = messege.from_user.full_name
    user_id = messege.from_user.id
    transliterated_name = translit(messege.text, 'ru', reversed=True)
    logging.info(f'{user_name} {user_id}: {messege.text}')
    await messege.answer(transliterated_name)

if __name__ == '__main__':# а было '__name__'
    dp.run_polling(bot)

logging.basicConfig(filename = "mylog.log")

