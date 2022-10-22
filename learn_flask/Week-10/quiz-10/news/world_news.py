import json
from flask import Blueprint, request, redirect, render_template
from bs4 import BeautifulSoup
import requests
from news.models import WorldNews
from news import db
from sqlalchemy import text, engine

cbsnews = Blueprint('cbsnews', __name__)

def get_cbs_news():

    world_url = "https://www.cbsnews.com/latest/world/"

    news_page = requests.get(world_url).text

    item = BeautifulSoup(news_page, 'lxml')

    world_page = item.find('div', {'class':'component__item-wrapper'})
    article_page = world_page.find_all('article', {'class':'item lazyload item--type-article item--topic-world'})

    cbs_news = []

    for item in article_page:
        title = item.find('div', {'class':'item__title-wrapper'}).h4.text.strip()
        link = item.a.get('href')
        image = item.span.img.get('src')
        description = item.find('div', {'class':'item__title-wrapper'}).p.text.strip()
        
        news_items = {'Title':title, 'Link':link, 'Image':image, 'Description':description} 
        news_items.update(news_items)

        cbs_news.append({
            'Title': title,
            'Link': link,
            'Image': image,
            'Description':description
        })

    return cbs_news


@cbsnews.route('/cbs-news', methods=['GET', 'POST'])
def cbs_news():
    if request.method == 'POST':
        return redirect('/')

    # new data from world news
    data = get_cbs_news()

    # existing data from database
    wnews =WorldNews.get_all_news()

    # loop through data
    for news in data:
        # check if news already exists in database
        # news['title'] is the title of the news
        if news.get('title').lower() not in [wn.title.lower() for wn in wnews]:
            wnews = WorldNews(title=news['title'], link=news['link'])
            wnews.save()
        else:
            continue

    return render_template('world_news.html', data=wnews)



@cbsnews.route('/world-news/search', methods=['GET', 'POST'])
def search_cbs_news():
    # /world-news/search?q=python
    query = request.args['q']
    # search in database for anythign that matches the query
    # SELECT * FROM world_news WHERE title LIKE '%python%'
    # data = db.session.query(worldNews).filter(worldNews.title.like(f'%{query}%')).all()
    # sql = text('SELECT * FROM world_news WHERE title LIKE :query')
    # data = db.engine.execute(sql, query=f'%{query}%').fetchall()
    data = WorldNews.query.filter(WorldNews.title.like(f'%{query}%')).all()
    # print(data)
    # [<HackNews 1>, <HackNews 2>]
    return {'data': [news.serialize() for news in data]}


@cbsnews.route('/search')
def search():
    return render_template('search.html')