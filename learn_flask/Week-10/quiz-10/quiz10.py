import requests
from bs4 import BeautifulSoup
import csv
world_url = "https://www.cbsnews.com/latest/world/"

news_page = requests.get(world_url).text

item = BeautifulSoup(news_page, 'lxml')

world_page = item.find('div', {'class':'component__item-wrapper'})
article_page = world_page.find_all('article', {'class':'item lazyload item--type-article item--topic-world'})

news_items = {}

for item in article_page:
    title = item.find('div', {'class':'item__title-wrapper'}).h4.text.strip()
    link = item.a.get('href')
    image = item.span.img.get('src')
    description = item.find('div', {'class':'item__title-wrapper'}).p.text.strip()
    
    news_items = {'Title':title, 'Link':link, 'Image':image, 'Description':description} 
    news_items.update(news_items)

# with open('news.csv', 'w') as new:

#     fieldnames = ['Title', 'Link', 'Image', 'Description']
#     writer = csv.DictWriter(new, fieldnames=fieldnames)

#     writer.writerows(news_items.values())


# print('Done')
        