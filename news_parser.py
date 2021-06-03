from bs4 import BeautifulSoup
import urllib.request

req = urllib.request.urlopen('https://ria.ru/')
html = req.read()

soup = BeautifulSoup(html, 'html.parser')
news = soup.find_all('div', class_='cell-list__item m-no-image')

results = []
for item in news:
    title = item.find('span', class_ = 'cell-list__item-title').get_text()
    href = item.name_list.get('href')
    results.append({
        'title': title,
        'href': href
    })
print(results)

with open('news.txt', 'w', encoding='utf-8') as file:
    i = 1
    for item in results:
        file.write(f'Новость №{i}\n\nНазвание: {item["title"]}\nСсылка: {item["href"]}\n\n****************\n\n')
        i += 1