import requests
from bs4 import BeautifulSoup

def get_over25_games():
    results = {
        "predictz": [],
        "forebet": []
    }

    # ---------- PREDICTZ ----------
    try:
        url = "https://www.predictz.com/predictions/"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        games = soup.select(".predictions .prediction")
        for game in games:
            teams = game.select_one(".teams")
            if teams:
                results["predictz"].append(teams.text.strip())

    except Exception as e:
        print("PredictZ scraping error:", e)

    # ---------- FOREBET ----------
    try:
        url = "https://www.forebet.com/en/football-predictions"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        matches = soup.select(".prediction")
        for match in matches:
            teams = match.select_one(".homeTeam")
            away = match.select_one(".awayTeam")
            if teams and away:
                results["forebet"].append(teams.text.strip() + " vs " + away.text.strip())

    except Exception as e:
        print("Forebet scraping error:", e)

    return results
