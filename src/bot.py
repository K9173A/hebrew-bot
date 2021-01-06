import os

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor, types

from src.action import Action
from src.api import process_action


load_dotenv()

token = os.getenv('BOT_TOKEN')
bot = Bot(token=token)
dispatcher = Dispatcher(bot=bot)


@dispatcher.message_handler(commands=['start'])
async def on_start(message: types.Message) -> None:
    """
    Handles /start command. Displays available buttons for actions.

    :param message: message object.
    :return: answer.
    """
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton(text=Action.CURRENT_EVENTS))
    keyboard.add(types.KeyboardButton(text=Action.CURRENT_DATE))
    await message.answer('Выберите действие:', reply_markup=keyboard)


@dispatcher.message_handler()
async def on_message(message: types.Message) -> None:
    """
    Handles messages from user.

    :param message: message object.
    :return: answer.
    """
    reply_text = process_action(message.text)
    await message.answer(reply_text, reply_markup=types.ReplyKeyboardRemove())


if __name__ == '__main__':
    executor.start_polling(dispatcher=dispatcher, skip_updates=True)
