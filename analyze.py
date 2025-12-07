def calculate_confidence(match_entries):
    """
    Confidence = number of prediction sources * 20%
    Max 100%.
    """
    sources = len(match_entries)
    confidence = min(sources * 20, 100)
    return confidence


def filter_top_games(match_data):
    # Dictionary to combine predictions for same match
    combined = {}

    for site, predictions in match_data.items():
        for match, pred in predictions:
            if "2.5" in pred:

                if match not in combined:
                    combined[match] = []

                combined[match].append({
                    "source": site,
                    "prediction": pred
                })

    results = []

    for match, entries in combined.items():
        confidence = calculate_confidence(entries)

        results.append({
            "match": match,
            "prediction": entries[0]["prediction"],
            "sources": [e["source"] for e in entries],
            "confidence": confidence
        })

    # Sort by confidence (high → low)
    results_sorted = sorted(results, key=lambda x: x["confidence"], reverse=True)

    top5 = results_sorted[:5]
    top10 = results_sorted[:10]

    return top5, top10
