import requests
from bs4 import BeautifulSoup

def get_predictz():
    url = "https://www.predictz.com/predictions/"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "lxml")

    results = []
    for row in soup.select(".predtable tr"):
        cols = row.find_all("td")
        if len(cols) > 4:
            match = cols[0].text.strip()
            prediction = cols[4].text.strip()
            if "2.5" in prediction:
                results.append((match, prediction))
    return results

def scrape_all():
    data = {
        "predictz": get_predictz(),
        "soccervista": [],
        "forebet": [],
        "betclan": []
    }
    return data

if __name__ == "__main__":
    print(scrape_all())
