"""Создать базу пользователей. Запускается один раз."""
import sqlite3
from config import Config

try:
    db_connection = sqlite3.connect(Config.database)
    db_cursor = db_connection.cursor()

    users_table_create_sql_command = """CREATE TABLE users(
                                        username TEXT UNIQUE
                                        );"""

    db_cursor.execute(users_table_create_sql_command)
    db_connection.commit()
    db_cursor.close()
    db_connection.close()
except Exception as ex:
    print(ex)
