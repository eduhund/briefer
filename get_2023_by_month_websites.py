from datetime import datetime
from generate_date_interval import generate_date_interval
from save_websites_for_launch_date import save_websites_for_launch_date

interval = generate_date_interval(datetime(2023, 7, 1), datetime(2023, 7, 26))

for day in interval:
    save_websites_for_launch_date(day)