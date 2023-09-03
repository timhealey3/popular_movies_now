# what movie/tv show to watch
# webscraping imdb to find most popular movies
import requests
from bs4 import BeautifulSoup


def netflix_data():
    url_netflix = "https://www.netflix.com/tudum/top10"

    headers = {"Accept-Language": "en-US, en;q=0.5"}

    results_netflix = requests.get(url_netflix, headers=headers)

    netflix_soup = BeautifulSoup(results_netflix.text, "html.parser")

    netflix_rank = []
    netflix_name = []
    netflix_views = []

    for tag in netflix_soup.find_all('tr'):
        first_name = tag.find('td', class_ = 'pb-2 tbl-cell tbl-cell-name pt-2')
        first_views = tag.find('td', class_ = 'pb-2 tbl-cell tbl-cell-vhor pt-2')
        name = tag.find('td', class_ = 'pb-2 tbl-cell tbl-cell-name')
        views = tag.find('td', class_ = 'pb-2 tbl-cell tbl-cell-vhor')
        if first_name is not None:
            netflix_name.append(first_name.get_text())
            netflix_views.append(first_views.get_text())
        if name is not None:
            netflix_name.append(name.get_text())
            netflix_views.append(views.get_text())

    return netflix_name
