from selenium import webdriver
from selenium.webdriver.common.by import By

from product_hunt_url_by_nick import product_hunt_url_by_nick
from open_webpage_by_url import open_webpage_by_url

def get_website_of_product(product):
    """Вытаскивает вебсайт со страницы продукта"""
    # TODO Не слишком ли тут много вложенности?
    url = product_hunt_url_by_nick(product)
    webpage = open_webpage_by_url(url)
    xpath = '//a[@data-test="product-header-visit-button"]'
    ahref = webpage.find_element(By.XPATH, xpath)
    href_with_ref = ahref.get_attribute('href')
    pure_href = href_with_ref.split('?')[0]
    # TODO Слишком много функциональности в одной функции

    return pure_href

if __name__ == '__main__':
    print(get_website_of_product('jasper-6'))