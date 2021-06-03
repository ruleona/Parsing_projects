import requests
from bs4 import BeautifulSoup
import csv

HOST = 'https://novayagazeta.ru/'
URL = 'https://novayagazeta.ru/news/'
HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
}
def get_html(url, params=''):
    r = requests.get(url, headers=HEADERS, params=params)
    return r

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('a', class_='_4-Kgf material-reference')
    articles = []
    print(items)

html = get_html(URL)
get_content(html)

    # for item in items:
    #     articles.append(
    #         {
    #             'title': item.find('div', class_='RichBlock-title').get_text(),
    #             'link': item.find('h3', class_='RichBlock-title').find('a').get('href'),
    #             # 'price': item.find('div',
    #             #                    class_='iva-item-priceStep-2qRpg').get_text(),
    #             # 'image_of_ap': item.find('div', class_='photo-slider-item-15V4q photo-slider-keepImageRatio-1bSLF').find('img').get('src')
    #         }
    #     )
    # return apartments