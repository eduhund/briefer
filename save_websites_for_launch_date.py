from datetime import datetime
from generate_date_interval import generate_date_interval
from get_launch_dataframe_from_file import get_launch_dataframe_from_file
from add_websites_to_dataframe import add_websites_to_dataframe

def save_websites_for_launch_date(date):
    """Сохраняем вебсайты проектов на конкретную дату"""
    # TODO Убрать константы

    WEBSITES_ARCHIVE = 'websites/'

    # TODO Убрать вложенность? Вообще криво как-то с этим сохранением
    ldf = get_launch_dataframe_from_file(date)
    wdf = add_websites_to_dataframe(ldf)
    wdf.to_pickle(f"{WEBSITES_ARCHIVE}{date.year}-{date.month}-{date.day}.pkl")

    return True

if __name__ == '__main__':
    save_websites_for_launch_date(datetime(2023,5,1))