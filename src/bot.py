import os

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor, types

from action import Action
from api import process_action


load_dotenv()

token = os.getenv('BOT_TOKEN')
bot = Bot(token=token)
dispatcher = Dispatcher(bot=bot)


@dispatcher.message_handler(commands=['start'])
async def on_start(message: types.Message) -> None:
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton(text=Action.GET_TODAY_INFORMATION))
    await message.answer('Hello from HebrewInfoBot! Choose action:', reply_markup=keyboard)


@dispatcher.message_handler()
async def on_message(message: types.Message) -> None:
    reply_text = process_action(message.text.lower())
    await message.answer(reply_text, reply_markup=types.ReplyKeyboardRemove())


if __name__ == '__main__':
    executor.start_polling(dispatcher=dispatcher, skip_updates=True)
