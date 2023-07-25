def product_nick_from_url(url):
    """Извлекает ник продукта из полного (и даже избыточного) URL'а"""
    skip_hash = url.split('#')[0]
    nick_as_a_last_part_of_url = skip_hash.split('/')[-1]
    
    return nick_as_a_last_part_of_url

if __name__ == '__main__':
    URL = 'https://www.producthunt.com/products/twinr-app-builder#twinr-2-0'

    print(product_nick_from_url(URL))