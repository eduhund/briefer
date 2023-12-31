from selenium.webdriver.common.by import By
from open_webpage_by_url import open_webpage_by_url

def get_all_links_from_webpage(webpage):
    """Получить все ссылки со страницы"""
    ahrefs = webpage.find_elements(By.TAG_NAME, 'a')

    all_links = set()
    for a in ahrefs:
        # TODO Переписать на задержках или хотя бы на точном исключении
        try:
            href = a.get_attribute('href')
            all_links.add(href)
        except:
            pass

    return list(all_links)

if __name__ == '__main__':
    URL = 'https://www.producthunt.com/time-travel/2023/2/20'

    webpage = open_webpage_by_url(URL)
    all_links = get_all_links_from_webpage(webpage)

    print(all_links)