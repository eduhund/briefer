from selenium import webdriver

def open_webpage_by_url(url):
    """Открыть страницу по URL"""
    webpage = webdriver.Safari()
    webpage.implicitly_wait(10)
    webpage.get(url)
    return webpage

if __name__ == '__main__':
    URL = 'https://www.producthunt.com/time-travel/2023/2/20'
    b = open_webpage_by_url(URL)
    print(b.title)