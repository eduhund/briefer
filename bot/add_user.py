from aiogram import types
from check_user_has_username import check_user_has_username
from add_user_to_db import add_user_to_db

def add_user(message: types.message):
    if check_user_has_username(message):
        add_user_to_db(message.chat.username)