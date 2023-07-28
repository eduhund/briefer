import os.path
import time
from open_webpage_by_url import open_webpage_by_url

def save_screenshort_by_url(nick, url):
    # TODO Убрать мнимую независимость ника и урла

    # TODO Убрать константу из кода
    SHOTS_ARCHIVE = 'shots/'
    # TODO Убрать дублирование функциональности (проверка файла на существование — лишняя)
    file_path = f"{SHOTS_ARCHIVE}{nick}.png"
    if url and (not os.path.exists(file_path)):
        try:
            webpage = open_webpage_by_url(url)
            time.sleep(5)
            webpage.save_screenshot(file_path)
            webpage.close()
        except Exception as ex:
            print(f"save screenshot by url: {nick} — {url}")

    return True

if __name__ == '__main__':
    save_screenshort_by_url('vk', 'https://www.vk.com')
    