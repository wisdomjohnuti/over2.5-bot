def calculate_confidence(match_data):
    """
    Very simple confidence model:
    - More sources agreeing = higher score.
    - Returned as percentage (0–100%).
    """
    score = 0
    sources = 0

    for site, predictions in match_data.items():
        for match, pred in predictions:
            if "2.5" in pred:
                score += 20       # each site increases confidence
                sources += 1

    confidence = min(score, 100)
    return confidence


def filter_top_games(match_data):
    results = []

    # Flatten data into a list of unique matches
    for site, predictions in match_data.items():
        for match, pred in predictions:
            if "2.5" in pred:
                results.append({
                    "match": match,
                    "prediction": pred,
                    "source": site
                })

    # Fake scoring for now (real scoring comes later)
    # Sort alphabetically to keep simple structure
    results_sorted = sorted(results, key=lambda x: x["match"])

    # Top 5 and Top 10 lists
    top5 = results_sorted[:5]
    top10 = results_sorted[:10]

    return top5, top10


if __name__ == "__main__":
    sample = {
        "predictz": [("Team A vs Team B", "Over 2.5")],
        "forebet": [("Team A vs Team B", "Over 2.5")],
        "soccervista": [],
        "betclan": [],
    }

    top5, top10 = filter_top_games(sample)
    print("TOP 5:", top5)
    print("TOP 10:", top10)
