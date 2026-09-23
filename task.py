# Placeholder classifier: predicts guard ("G") for shorter players.
HEIGHT_THRESHOLD = 78  # inches (6'6")


def classify(height, positive):
    if positive == "G":
        return "positive" if height < HEIGHT_THRESHOLD else "negative"
    return "negative"
