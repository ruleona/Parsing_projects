import requests
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import csv

HOST = 'https://www.avito.ru/'
URL = 'https://www.avito.ru/nizhniy_novgorod/kvartiry/sdam/'
HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
}
# I used Firefox; you can use whichever browser you like.
browser =  webdriver.Chrome(ChromeDriverManager().install())



def get_html():
    # Tell Selenium to get the URL you're interested in.
    browser.get(URL)
    # Selenium script to scroll to the bottom, wait 3 seconds for the next batch of data to load, then continue scrolling.  It will continue to do this until the page stops loading new data.
    lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    match=False
    while(match==False):
        lastCount = lenOfPage
        time.sleep(2)
        lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
        if lastCount==lenOfPage:
            match=True
    return browser.page_source.encode('utf-8')


def get_image(item):
    bs_image = item.find('img', class_='photo-slider-image-1fpZZ')
    if bs_image is None:
        return 'Not find'
    else:
        return bs_image.get('src')

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
                'image_of_ap': get_image(item)
            }
        )
    return apartments


print(get_content(get_html()))

browser.close()