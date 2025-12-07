import requests
from bs4 import BeautifulSoup

def scrape_predictz():
    url = "https://www.predictz.com/predictions/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")

    games = []
    for match in soup.select(".ptn"):
        try:
            teams = match.select_one(".ptnmt").get_text(strip=True)
            prediction = match.select_one(".ptnpr").get_text(strip=True)

            if "Over 2.5" in prediction:
                games.append(teams)
        except:
            continue

    return games


def scrape_forebet():
    url = "https://www.forebet.com/en/football-predictions"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")

    games = []
    for match in soup.select(".rcnt"):
        try:
            teams = match.select_one(".homeTeam").get_text(strip=True) + " vs " + match.select_one(".awayTeam").get_text(strip=True)
            prediction = match.select_one(".predict").get_text(strip=True)

            if "Over 2.5" in prediction:
                games.append(teams)
        except:
            continue

    return games


def get_over25_games():
    games = []
    games.extend(scrape_predictz())
    games.extend(scrape_forebet())
    return games
