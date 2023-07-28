from selenium import webdriver

def open_webpage_by_url(url):
    """Открыть страницу по URL"""
    webpage = webdriver.Safari()
    # TODO Вынести отдельно настройку размера для скриншотов
    webpage.set_window_size(1280,1280+52)
    webpage.implicitly_wait(10)
    # TODO В чём на самом деле проблема с открытием страниц?
    try:
        webpage.get(url)
    except Exception as ex:
        print(f"open webpage error: {ex}")
    return webpage

if __name__ == '__main__':
    URL = 'https://www.producthunt.com/time-travel/2023/2/20'
    b = open_webpage_by_url(URL)
    print(b.title)
    