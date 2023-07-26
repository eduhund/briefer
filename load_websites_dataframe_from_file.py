import pandas as pd
from datetime import datetime

def load_websites_dataframe_from_file(date):
    """Получить датафрейм конкретного дня из файла"""
    # TODO Убрать константу из кода
    WEBSITES_ARCHIVE = 'websites/' 

    # TODO Убрать вложенность? Вообще криво как-то с этим сохранением
    ldf = pd.read_pickle(f"{WEBSITES_ARCHIVE}{date.year}-{date.month}-{date.day}.pkl")

    return ldf

if __name__ == '__main__':
    print(load_websites_dataframe_from_file(datetime(2023,4,28)))