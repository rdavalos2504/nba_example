from task import classify
from data import players


def score(truth, response):
    if truth == "positive":
        return "tp" if response == "positive" else "fn"
    return "tn" if response == "negative" else "fp"


def safe_div(numerator, denominator):
    return numerator / denominator if denominator else 0.0


def run_eval(players, positive):
    counts = {"tp": 0, "tn": 0, "fp": 0, "fn": 0}
    for name, position, height, ppg, rpg, apg in players:
        if position == positive:
            truth = "positive"
        else:
            truth = "negative"
        response = classify(height, positive)
        print(height, truth, response)
        counts[score(truth, response)] += 1
    precision = safe_div(counts["tp"], counts["tp"] + counts["fp"])
    recall = safe_div(counts["tp"], counts["tp"] + counts["fn"])
    print(f"precision = {precision}")
    print(f"recall = {recall}")
    for key in counts:
        print(f"{key} = {counts[key]}")


run_eval(players, "G")
