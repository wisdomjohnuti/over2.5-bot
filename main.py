from scripts.scraper import get_over25_games
from analyze import filter_top_games

def run():
    print("🔎 Scraping...")
    data = get_over25_games()

    print("DEBUG OUTPUT:", data)

    print("📊 Analyzing...")
    top5, top10 = filter_top_games(data)

    print("---- TOP 5 GAMES ----")
    for g, s in top5:
        print(g, s)

if __name__ == "__main__":
    run()
