import requests
from bs4 import BeautifulSoup


def scrape_predictz():
    url = "https://www.predictz.com/predictions/"
    games = []

    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, "lxml")

        for match in soup.select(".ptn"):
            try:
                teams = match.select_one(".ptnmt").get_text(strip=True)
                prediction = match.select_one(".ptnpr").get_text(strip=True)

                if "Over 2.5" in prediction:
                    games.append((teams, prediction))
            except:
                continue
    except:
        print("⚠ PredictZ scraping failed")

    return games


def scrape_forebet():
    url = "https://www.forebet.com/en/football-predictions"
    games = []

    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, "lxml")

        for match in soup.select(".rcnt"):
            try:
                home = match.select_one(".homeTeam").get_text(strip=True)
                away = match.select_one(".awayTeam").get_text(strip=True)
                prediction = match.select_one(".predict").get_text(strip=True)

                teams = f"{home} vs {away}"

                if "Over 2.5" in prediction:
                    games.append((teams, prediction))
            except:
                continue
    except:
        print("⚠ Forebet scraping failed")

    return games


def scrape_all():
    """
    MUST return dictionary with this structure:
    {
        "predictz": [(match, prediction), ...],
        "forebet": [(match, prediction), ...]
    }
    """
    return {
        "predictz": scrape_predictz(),
        "forebet": scrape_forebet(),
    }


if __name__ == "__main__":
    print(scrape_all())
