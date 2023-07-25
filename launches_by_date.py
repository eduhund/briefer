import pandas as pd
from datetime import datetime
from time_travel_url_by_date import time_travel_url_by_date
from open_webpage_by_url import open_webpage_by_url
from get_all_links_from_webpage import get_all_links_from_webpage
from product_links_only import product_links_only
from product_nick_from_url import product_nick_from_url

def launches_by_date(date):
    launches_list_url = time_travel_url_by_date(date)
    launches_webpage = open_webpage_by_url(launches_list_url)
    launches_link_list = product_links_only(get_all_links_from_webpage(launches_webpage))
    launches_list = [product_nick_from_url(i) for i in launches_link_list]
    return launches_list

if __name__ == '__main__':
    print(launches_by_date(datetime(2022, 11, 25)))