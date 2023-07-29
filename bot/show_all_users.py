import sqlite3
from config import Config

def show_all_users():
    try:
        # TODO Можно вынести соединение с базой данных в отдельную функцию?
        db_connection = sqlite3.connect(Config.database)
        db_cursor = db_connection.cursor()

        show_all_users_sql = "SELECT username FROM users;"

        db_cursor.execute(show_all_users_sql)
        all_users = db_cursor.fetchall()
        db_connection.commit()
        db_cursor.close()
        db_connection.close()
    except Exception as ex:
        # TODO Нужна нормальная обработка ошибок
        print(ex)

    return all_users

if __name__ == '__main__':
    print(show_all_users())
