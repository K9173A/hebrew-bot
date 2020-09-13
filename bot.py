import os

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor, types

from log import initialize_logger
from date_converter import get_hebrew_date

initialize_logger()
load_dotenv()

token = os.getenv('BOT_TOKEN')
bot = Bot(token=token)
dispatcher = Dispatcher(bot=bot)


@dispatcher.message_handler(commands=['start'])
async def on_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

    keyboard.add(types.KeyboardButton(text='Date converter'))
    keyboard.add(types.KeyboardButton(text='???'))

    await message.answer('Hello from HebrewInfoBot! Choose action:', reply_markup=keyboard)


@dispatcher.message_handler()
async def on_message(message: types.Message):
    text = message.text.lower()

    if text == 'date converter':
        reply_text = 'Specify year/month/day'
    elif text == 'cancel':
        reply_text = 'Canceled'
    else:
        reply_text = get_hebrew_date(*text.split('/'))
    # else:
    #     reply_text = 'Can\'t recognize specified command. Try /help to start.'

    await message.answer(reply_text, reply_markup=types.ReplyKeyboardRemove())


if __name__ == '__main__':
    executor.start_polling(dispatcher=dispatcher, skip_updates=True)
