from config import Config
from aiogram import Bot, Dispatcher, executor, types

bot = Bot(token=Config.token)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def welcome(message: types.message):
    await message.answer('Привет-привет')

@dp.message_handler()
async def echo(message: types.message):
    await message.reply(message.chat.username)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)