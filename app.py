from flask import Flask, request, jsonify
from scraper.scraper import get_reviews
from sentiment.sentiment import analyze_sentiment

app = Flask(__name__)


# Home route (just to check server is running)
@app.route("/")
def home():
    return "Product Sentiment Analyzer Backend Running"


# Main API route
@app.route("/analyze-product", methods=["POST"])
def analyze_product():
    data = request.get_json()

    # Validate input
    if not data or "url" not in data:
        return jsonify({"error": "Product review URL is required"}), 400

    product_url = data["url"]

    # Step 1: Scrape reviews
    reviews = get_reviews(product_url)

    # Step 2: Sentiment analysis
    summary = {
        "Positive": 0,
        "Negative": 0,
        "Neutral": 0
    }

    final_reviews = []

    for r in reviews:
        sentiment = analyze_sentiment(r["text"])
        summary[sentiment] += 1
        final_reviews.append({
            "text": r["text"],
            "sentiment": sentiment
        })

    # Step 3: Return JSON response
    return jsonify({
        "summary": summary,
        "reviews": final_reviews
    })


if __name__ == "__main__":
    app.run(debug=True)
