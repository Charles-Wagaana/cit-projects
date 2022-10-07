import requests
from bs4 import BeautifulSoup

git_user = input('Enter github username: ')
url = 'https://github.com/'+git_user

response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

profile_image = soup.find('img', class_="avatar avatar-user width-full border color-bg-default")['src']

print(profile_image)