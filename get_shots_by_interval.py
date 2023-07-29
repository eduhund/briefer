from datetime import datetime
from generate_date_interval import generate_date_interval
from save_shots_for_launch_day import save_shots_for_launch_day

interval = generate_date_interval(datetime(2023, 5, 20), datetime(2023, 7, 25))

for day in interval:
    print(day)
    try:
        save_shots_for_launch_day(day)
    except Exception as ex:
        print(f" — {ex}")
    