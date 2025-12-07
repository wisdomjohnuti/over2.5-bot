def filter_top_games(data):
    top5 = []
    top10 = []

    # combine both websites
    combined = data["predictz"] + data["forebet"]

    # Dummy scoring (you will improve later)
    for game in combined:
        score = len(game)  # simple scoring
        top10.append((game, score))

    top10 = sorted(top10, key=lambda x: x[1], reverse=True)
    top5 = top10[:5]

    return top5, top10
