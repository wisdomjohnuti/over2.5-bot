import os
import requests


def send_message(text):
    """
    Sends a message to your Telegram bot.
    Telegram bot token and chat ID must be stored in GitHub Secrets.
    """
    token = os.environ.get("TELEGRAM_BOT_TOKEN")
    chat_id = os.environ.get("TELEGRAM_CHAT_ID")

    if not token or not chat_id:
        print("❌ Missing Telegram credentials!")
        return

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "HTML",
    }

    try:
        requests.post(url, data=payload)
        print("✅ Message sent to Telegram")
    except Exception as e:
        print("❌ Error sending message:", e)


def format_message(top5, top10):
    """
    Formats the message nicely for Telegram.
    Includes confidence and number of sources.
    """
    text = "<b>🔥 TOP OVER 2.5 PICKS 🔥</b>\n\n"

    text += "<b>TOP 5 OVER 2.5:</b>\n"
    for item in top5:
        sources_count = len(item.get("sources", []))
        text += (
            f"• <b>{item['match']}</b>\n"
            f"  ↳ {item['prediction']} | "
            f"<i>{item['confidence']}% confidence</i> | "
            f"{sources_count} sources\n"
        )

    text += "\n<b>TOP 10 OVER 2.5:</b>\n"
    for item in top10:
        sources_count = len(item.get("sources", []))
        text += (
            f"• <b>{item['match']}</b>\n"
            f"  ↳ {item['prediction']} | "
            f"<i>{item['confidence']}% confidence</i> | "
            f"{sources_count} sources\n"
        )

    return text


if __name__ == "__main__":
    # Local test example
    sample5 = [{
        "match": "Team A vs Team B",
        "prediction": "Over 2.5",
        "confidence": 85,
        "sources": ["predictz", "forebet"]
    }]

    sample10 = [{
        "match": "Team C vs Team D",
        "prediction": "Over 2.5",
        "confidence": 72,
        "sources": ["forebet"]
    }]

    msg = format_message(sample5, sample10)
    print(msg)
