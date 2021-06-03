import requests
from bs4 import BeautifulSoup
import csv

HOST = 'https://www.avito.ru/'
URL = 'https://www.avito.ru/nizhniy_novgorod/kvartiry/sdam/'
HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
}
def get_html(url, params=''):
    r = requests.get(url, headers=HEADERS, params=params)
    return r

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='iva-item-content-m2FiN')
    apartments = []

    for item in items:
        apartments.append(
            {
                'title': item.find('div', class_='iva-item-body-NPl6W').get_text(),
                'link': item.find('a', class_='link-link-39EVK').get('href'),
                'price': item.find('span', class_='price-text-1HrJ_').get_text(),
                'image_of_ap': item.find('img', class_='photo-slider-image-1fpZZ').get('src')
            }
        )
    return apartments

html = get_html(URL)
print(get_content(html.text))
