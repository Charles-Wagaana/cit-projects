# Question 1
import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"

response = requests.get(url).text

soup = BeautifulSoup(response, 'html.parser')

movie_list = soup.find('tbody', {'class':'lister-list'})
movie_rows = movie_list.find_all('tr')

items_found = {}

for index, movie in enumerate(movie_rows):

    movie_url = "https://www.imdb.com" + movie.find('td', {'class':'titleColumn'}).find('a').get('href')
    
    response = requests.get(movie_url).text

    movie_soup = BeautifulSoup(response, 'html.parser')

    
    movie_year = movie_soup.find('div', {'class':'sc-80d4314-2 iJtmbR'}).ul.li.find('a', {'class':'ipc-link ipc-link--baseAlt ipc-link--inherit-color sc-8c396aa2-1 WIUyh'}).get_text()
    if int(movie_year) > 1980:
    # movie_duration = movie_soup.find('div', {'class':'sc-80d4314-2 iJtmbR'}).ul.find('li', {'class':'ipc-inline-list__item'})[1].get_text()
        movie_title = movie_soup.find('div', {'class':'sc-80d4314-1 fbQftq'}).find('h1').get_text()
    
        movie_description = movie_soup.find('span', class_ = 'sc-16ede01-2 gXUyNh').get_text()
        movie_director = movie_soup.find('div', {'class':'ipc-metadata-list-item__content-container'}).ul.li.a.get_text()
        
        movie_actors = movie_soup.find_all('div', {'class':'sc-36c36dd0-8 fSYMLK'})
        movie_rating = movie_soup.find('div', class_ = 'sc-f6306ea-3 loTxjn').span.get_text()
        # movie_reviews = movie_soup.find('div', {'class':'sc-80d4314-0 fjPRnj'}).find('span', class_ = 'score').get_text()
        movies_actor = [item.a.get_text() for index, item in enumerate(movie_actors)]
        # for index, item in enumerate(movie_actors):
        #     movie_actor = item.a.get_text()
        #     movies_actor.append(movie_actor)
            

        movie_genre = movie_soup.find('div', 'ipc-chip-list__scroller').a.get_text()
        # metascore = movie_soup.find('div', {'class':'sc-2a827f80-5 gcCaSg'}).ul.get_text()
    # movie_review = movie_soup.find('div', {'class':'sc-2a827f80-5 gcCaSg'}).find('span', {'claxss':'score'}).get_text()

        items_found[index+1] = {'Title':movie_title, 'Description':movie_description,
             'Director':movie_director, 'Genre':movie_genre, 
             'Year':movie_year, 'Actors':movies_actor, 'Rating':movie_rating}

        items_found = sorted(items_found.items(), key = lambda x: x[1]["Rating"], reverse=True)
        items_found = dict(items_found)

with open("movies.csv", "w") as file:
    writer = csv.writer(file)

    writer.writerows(items_found.items())

print("Done")

        # print(items_found)
    

# Question 2

hack_url = 'http://news.ycombinator.com/' 

response = requests.get(hack_url)

hack_soup = BeautifulSoup(response.text, 'html.parser')

items_found = {}

items_found1 = {}

hack = hack_soup.find('table', class_ = 'itemlist')
hack_rows = hack.find_all('tr', class_ = 'athing')

for index1, item1 in enumerate(hack_rows):
    title = item1.find('span', class_ = 'titleline').text
    link = item1.find('span', class_ = 'sitebit comhead').a.get('href')

    rank  = item1.find('span', class_ = 'rank').text.strip('.')
    
    items_found1 = {"Title": title, "Link": link, "Rank": rank}

    items_found.update(items_found1)

items_found2 = {}

sub_rows1 = hack.find_all('td', class_ = 'subtext')
    
for index2, item2 in enumerate(sub_rows1):
    sub_rows2 = item2.find_all('span', class_ = 'subline')

    for index3, item3 in enumerate(sub_rows2):
        
        author = item3.find('a', class_ = 'hnuser').text
        
    points = item2.find('span', class_ = 'score')
    
   
    if points is not None:
        points = points.text 

    items_found2 = {"Points": points, 'Author': author}
    
    items_found.update(items_found2)

    items_found = dict(items_found1.items())
    items_found.update(items_found2)

    # print(items_found)
    items_found = sorted(items_found.items(), key = lambda x: x[1]["Rank"])
    items_found = dict(items_found)

with open("news.csv", "w") as file:
    writer = csv.writer(file)

    writer.writerows(items_found.items())

print("Done")

# # print(items_found1)
        

    



    
