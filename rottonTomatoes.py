import requests
from bs4 import BeautifulSoup


def rotten_data():
    url_rotten = "https://editorial.rottentomatoes.com/guide/popular-movies/"

    headers = {"Accept-Language": "en-US, en;q=0.5"}

    results_rotten = requests.get(url_rotten, headers=headers)

    rotten_soup = BeautifulSoup(results_rotten.text, "html.parser")

    rotten_rank = []
    rotten_name = []
    rotten_score = []

    for tag in rotten_soup.find_all('h2'):
        name = tag.find('a')
        rank = tag.find('span', class_='subtle start-year')
        score = tag.find('span', class_='tMeterScore')
        if name is not None and rank is not None:
            rotten_name.append(name.get_text())
            rotten_rank.append(rank.get_text())
            rotten_score.append(score.get_text())

    return rotten_name
