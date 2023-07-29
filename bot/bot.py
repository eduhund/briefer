from config import Config
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from add_user import add_user
from show_all_users import show_all_users
from get_random_shot import get_random_shot

# TODO Вынести клавиатуру в отдельный модуль
kb = InlineKeyboardMarkup(row_width=4)
buttons = {
    'like': InlineKeyboardButton(text='like', callback_data='like'),
    'no': InlineKeyboardButton(text='no', callback_data='no'),
    'star': InlineKeyboardButton(text='star', callback_data='star'),
    'error': InlineKeyboardButton(text='error', callback_data='error')
    }

kb.add(buttons['like'], buttons['no'], buttons['star'], buttons['error'])
print(kb)

bot = Bot(token=Config.token)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def welcome(message: types.message):
    add_user(message)
    await message.answer(text='Привет-привет')

@dp.message_handler(commands=['vote'])
async def vote(message: types.message):
    random_shot_name = get_random_shot()
    random_shot = open(f"{Config.shots}/{random_shot_name}", 'rb')
    await message.answer_photo(photo=random_shot,
                                reply_markup=kb)

@dp.message_handler(commands=['all_users'])
async def all_users(message: types.message):
    await message.answer(show_all_users())

@dp.message_handler()
async def echo(message: types.message):
    await message.reply(message.chat.username)

@dp.callback_query_handler()
async def vote_response(callback: types.CallbackQuery):
    if callback.data == 'like':
        answer = 'Вы нажали кнопку Like'
    elif callback.data == 'no':
        answer = 'Вы нажали кнопку No'
    elif callback.data == 'star':
        answer = 'Вы нажали кнопку Star'
    elif callback.data == 'error':
        answer = 'Вы нажали кнопку Error'
    else:
        answer = 'Непонятно, что вы нажали'
    return await callback.answer(answer)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
    