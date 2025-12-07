def calculate_confidence(match_entries):
    """
    Confidence = number of prediction sources * 20%
    """
    sources = len(match_entries)
    confidence = min(sources * 20, 100)
    return confidence


def filter_top_games(match_data):
    combined = {}

    # match_data = {"predictz": [...], "forebet": [...]}
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
            "sources": [x["source"] for x in entries],
            "confidence": confidence
        })

    results_sorted = sorted(results, key=lambda x: x["confidence"], reverse=True)

    return results_sorted[:5], results_sorted[:10]
