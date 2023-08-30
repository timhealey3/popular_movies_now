# what movie/tv show to watch
# webscraping imdb to find most popular movies
import requests
from bs4 import BeautifulSoup


def netflix_data():
    url_netflix = "https://www.netflix.com/tudum/top10?week=2023-08-13"

    headers = {"Accept-Language": "en-US, en;q=0.5"}

    results_netflix = requests.get(url_netflix, headers=headers)

    netflix_soup = BeautifulSoup(results_netflix.text, "html.parser")

    netflix_rank = []
    netflix_name = []
    netflix_runtime = []
    netflix_views = []

    for tag in netflix_soup.find_all('tr'):
        first_rank = tag.find('td', class_ = 'pb-2 tbl-cell tbl-cell-rank pt-2')
        first_name = tag.find('td', class_ = 'pb-2 tbl-cell tbl-cell-name pt-2')
        first_runtime = tag.find('td', class_ = 'pb-2 tbl-cell tbl-cell-runtime pt-2')
        first_views = tag.find('td', class_ = 'pb-2 tbl-cell tbl-cell-vhor pt-2')
        rank = tag.find('td', class_ = 'pb-2 tbl-cell tbl-cell-rank')
        name = tag.find('td', class_ = 'pb-2 tbl-cell tbl-cell-name')
        runtime = tag.find('td', class_ = 'pb-2 tbl-cell tbl-cell-runtime')
        views = tag.find('td', class_ = 'pb-2 tbl-cell tbl-cell-vhor')
        if first_rank is not None:
            netflix_rank.append(first_rank.get_text())
            netflix_name.append(first_name.get_text())
            netflix_runtime.append(first_runtime.get_text())
            netflix_views.append(first_views.get_text())
        if rank is not None:
            netflix_rank.append(rank.get_text())
            netflix_name.append(name.get_text())
            netflix_runtime.append(runtime.get_text())
            netflix_views.append(views.get_text())

    return netflix_name
