import requests
from bs4 import BeautifulSoup


def imdb_data():
    url_imdb = 'https://www.imdb.com/search/title/?groups=top_100&ref_=adv_prv'

    headers = {"Accept-Language": "en-US, en;q=0.5"}

    results_imdb = requests.get(url_imdb, headers=headers)

    imdb_soup = BeautifulSoup(results_imdb.text, "html.parser")

    imdb_rank = []
    imdb_name = []
    imdb_score = []

    for tag in imdb_soup.find_all('h3'):
        name = tag.find('a')
        rank = tag.find('span', class_='lister-item-index unbold text-primary')
        #score = tag.find('div', class_='inline-block ratings-imdb-rating')['data-value']
        #print(score)
        if name is not None and rank is not None:
            imdb_name.append(name.get_text())
            imdb_rank.append(rank.get_text())
         #   imdb_score.append(score.get_text())

    return imdb_name
