from scripts.scraper import get_over25_games
from analyze import filter_top_games


def run():
    print("🔎 Scraping websites...")
    data = get_over25_games()

    print("📊 Analyzing data...")
    top5, top10 = filter_top_games(data)

    print("\n🔥 TOP 5 OVER 2.5 GAMES")
    for game in top5:
        print(game)

    print("\n🔥 TOP 10 OVER 2.5 GAMES")
    for game in top10:
        print(game)


if __name__ == "__main__":
    run()
