from datetime import datetime

def time_travel_url_by_date(date):
    """Сгенерить URL страницы с запусками по дате"""
    # TODO Убрать константу из кода
    TIME_TRAVEL = 'https://www.producthunt.com/time-travel/'
    url = f"{TIME_TRAVEL}{date.year}/{date.month}/{date.day}"
    return url

if __name__ == '__main__':
    url = time_travel_url_by_date(datetime(2023, 5, 23))
    print(url)