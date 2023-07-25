import pandas as pd
from datetime import datetime

def generate_date_interval(start, fin):
    """Выдать диапазон дат"""
    return pd.date_range(start, fin)

if __name__ == '__main__':
    print(generate_date_interval('2022-02-24', datetime.now()))