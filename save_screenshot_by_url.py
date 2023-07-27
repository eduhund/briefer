import time
from open_webpage_by_url import open_webpage_by_url

def save_screenshort_by_url(nick, url):
    # TODO Убрать мнимую независимость ника и урла
    webpage = open_webpage_by_url(url)
    webpage.set_window_size(1280,1280+52)
    time.sleep(5)

    # TODO Убрать константу из кода
    SHOTS_ARCHIVE = 'shots/'
    webpage.save_screenshot(f"{SHOTS_ARCHIVE}{nick}.png")

    return True

if __name__ == '__main__':
    save_screenshort_by_url('vk', 'https://www.vk.com')