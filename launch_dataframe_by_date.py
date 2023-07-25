import pandas as pd
from datetime import datetime
from launches_by_date import launches_by_date

def launch_dataframe_by_date(date):
    launches = launches_by_date(date)
    ldf = pd.DataFrame({'nick': launches, 'date': date})
    return ldf

if __name__ == '__main__':
    print(launch_dataframe_by_date(datetime(2022,10,8)))