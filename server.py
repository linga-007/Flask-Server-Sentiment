from flask import Flask, render_template, request, redirect, url_for
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

app = Flask(__name__)

nltk.download('vader_lexicon')


@app.route('/getdata' , methods=['POST'])
def index():
    data = request.json 
    print(data) 
    sia = SentimentIntensityAnalyzer()
    sentiment_score = sia.polarity_scores(data['data'])
    print(sentiment_score)
    # Get the sentiment scores
    positive = sentiment_score['pos']
    negative = sentiment_score['neg']


    # Calculate percentages
    total = positive + negative
    positive_percent = (positive / total)
    negative_percent = (negative / total)


    # Other sentiment (neutral)
    other_percent = 100 - (positive_percent + negative_percent )

    # Print results
    print("Sentiment Analysis Results:")
    print(f"Positive: {positive_percent:.2f}%")
    print(f"Negative: {negative_percent:.2f}%")
    print(f"Other: {other_percent:.2f}%")


    return [{"positive" :positive_percent, "negative" : negative_percent}]
 
@app.route('/test')
def success():
    return "Success"

if __name__ == '__main__':
    app.run(debug=True)