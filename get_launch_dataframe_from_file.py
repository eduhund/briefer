import pandas as pd
from datetime import datetime

def load_launch_dataframe_from_file(date):
    """Получить датафрейм конкретного дня из файла"""
    # TODO Убрать константу из кода
    LAUNCHES_ARCHIVE = 'launches/' 

    # TODO Убрать вложенность? Вообще криво как-то с этим сохранением
    ldf = pd.read_pickle(f"{LAUNCHES_ARCHIVE}{date.year}-{date.month}-{date.day}.pkl")

    return ldf

if __name__ == '__main__':
    print(load_launch_dataframe_from_file(datetime(2023,1,1)))