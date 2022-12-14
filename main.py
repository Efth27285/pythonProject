import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/List_of_highest-paid_film_actors"
url_text = requests.get(url).text
s = BeautifulSoup(url_text, 'lxml')
table = s.find('table')
table_links = table.find_all('a', href=True)
actors = []

for links in table_links:
    actors.append(links.get('href'))
print(actors)