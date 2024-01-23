import requests
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

def imdb_data():

    site= "https://www.imdb.com/search/title/?user_rating=1,&groups=top_100"
    # IMDB checks for user-agent. else giving 403 error
    headers = {'User-Agent': 'Mozilla/5.0'}
    req = Request(site,headers=headers)
    page = urlopen(req)
    imdb_soup = BeautifulSoup(page, 'html.parser')

    imdb_rank = []
    imdb_name = []
    imdb_score = []

    for x in imdb_soup.find_all('h3', class_='ipc-title__text'):
        imdb_name.append(x.text[3::])
    
    return imdb_name
