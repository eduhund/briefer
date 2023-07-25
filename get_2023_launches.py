from datetime import datetime
from generate_date_interval import generate_date_interval
from save_launch_dataframe_to_file import save_launch_dataframe_to_file

year = generate_date_interval(datetime(2023, 1, 1), datetime.now())

for day in year:
    save_launch_dataframe_to_file(day)