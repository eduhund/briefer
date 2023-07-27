from datetime import datetime
from load_websites_dataframe_from_file import load_websites_dataframe_from_file
from save_screenshot_by_url import save_screenshort_by_url

def save_shots_by_dataframe(df):
    for line in df.iterrows():
        save_screenshort_by_url(line[1].nick, line[1].website)

    return True

if __name__ == '__main__':
    save_shots_by_dataframe(load_websites_dataframe_from_file(datetime(2023,4,6)))