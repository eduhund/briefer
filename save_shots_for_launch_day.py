from datetime import datetime
from load_websites_dataframe_from_file import load_websites_dataframe_from_file
from save_shots_by_dataframe import save_shots_by_dataframe

def save_shots_for_launch_day(date):
    """Сохраняем вебсайты проектов на конкретную дату"""
    # TODO Убрать константы

    WEBSITES_ARCHIVE = 'websites/'
    SHOTS_ARCHIVE = 'shots/'

    # TODO Убрать вложенность? Вообще криво как-то с этим сохранением
    wdf = load_websites_dataframe_from_file(date)
    save_shots_by_dataframe(wdf)

    return True

if __name__ == '__main__':
    save_shots_for_launch_day(datetime(2023,5,1))