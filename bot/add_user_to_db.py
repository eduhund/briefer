import sqlite3
from config import Config

def add_user_to_db(username):
    try:
        # TODO Можно вынести соединение с базой данных в отдельную функцию?
        db_connection = sqlite3.connect(Config.database)
        db_cursor = db_connection.cursor()

        add_user_sql = f"""INSERT OR IGNORE
                            INTO users
                            VALUES ('{username}');"""

        db_cursor.execute(add_user_sql)
        db_connection.commit()
        db_cursor.close()
        db_connection.close()
    except Exception as ex:
        # TODO Нужна нормальная обработка ошибок
        print(ex)

if __name__ == '__main__':
    add_user_to_db('noone')