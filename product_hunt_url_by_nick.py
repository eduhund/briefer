def product_hunt_url_by_nick(nick):
    """Сгенерить URL страницы продукта по нику"""
    # TODO Убрать константу из кода (плюс она дублируется в другой функции)
    PRODUCT_URL = 'https://www.producthunt.com/products/'
    url = f"{PRODUCT_URL}{nick}"
    return url

if __name__ == '__main__':
    url = product_hunt_url_by_nick('eduhund')
    print(url)