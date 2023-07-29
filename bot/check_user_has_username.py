from aiogram import types

# TODO Как выглядит отсутствие ника? Пустая строка? Отсутствие поля?
def check_user_has_username(message: types.message):
    if message.chat.username:
        return True
    else:
        return False