from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

class SentimentAnalyzer:
    def __init__(self):
        self.vader_analyzer = SentimentIntensityAnalyzer()

    def analyze_text_textblob(self, text: str):
        blob = TextBlob(text)
        return {'polarity': blob.sentiment.polarity, 'subjectivity': blob.sentiment.subjectivity}

    def analyze_text_vader(self, text: str):
        return self.vader_analyzer.polarity_scores(text)