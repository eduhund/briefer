import pandas as pd
from datetime import datetime
from launch_dataframe_by_date import launch_dataframe_by_date

def save_launch_dataframe_to_file(date):
    """Сохранить датафрейм конкретного дня в файл"""
    # TODO Убрать константу из кода
    LAUNCHES_ARCHIVE = 'launches/' 

    # TODO Убрать вложенность? Вообще криво как-то с этим сохранением
    ldf = launch_dataframe_by_date(date)
    ldf.to_pickle(f"{LAUNCHES_ARCHIVE}{date.year}-{date.month}-{date.day}.pkl")

    return True

if __name__ == '__main__':
    save_launch_dataframe_to_file(datetime(2023,1,1))