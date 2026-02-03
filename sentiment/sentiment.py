from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Create analyzer object (loads VADER lexicon internally)
analyzer = SentimentIntensityAnalyzer()

def analyze_sentiment(text):
    # Get sentiment scores
    score = analyzer.polarity_scores(text)["compound"]

    # Decide label based on compound score
    if score >= 0.05:
        return "Positive"
    elif score <= -0.05:
        return "Negative"
    else:
        return "Neutral"


# TEST BLOCK — to check if this file works alone
if __name__ == "__main__":
    print(analyze_sentiment("This phone is amazing"))
    print(analyze_sentiment("Worst phone ever"))
    print(analyze_sentiment("Phone is okay"))

