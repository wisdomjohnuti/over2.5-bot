from scraper import scrape_all
from analyze import filter_top_games
from send_telegram import send_message, format_message


def run():
    print("🔎 Scraping websites...")
    data = scrape_all()

    print("📊 Analyzing data...")
    top5, top10 = filter_top_games(data)

    print("✈ Sending to Telegram...")
    text = format_message(top5, top10)
    send_message(text)

    print("✅ Done!")


if __name__ == "__main__":
    run()
