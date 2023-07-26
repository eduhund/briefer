import pandas as pd
from datetime import datetime
from get_website_of_product import get_website_of_product
from get_launch_dataframe_from_file import load_launch_dataframe_from_file

def add_websites_to_dataframe(df):
    """Добавить колонку с вебсайтами в датафрейм"""
    # TODO Нельзя ли поизящней вставлять колонку?
    web = df.nick.apply(lambda row: get_website_of_product(row))
    df.insert(2, 'website', web)
    return df

if __name__ == '__main__':
    print(add_websites_to_dataframe(load_launch_dataframe_from_file(datetime(2023,7,4))))