# assessments/mood_assessment.py
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def assess_mood():
    nltk.download('vader_lexicon')
    analyzer = SentimentIntensityAnalyzer()
    
    print("How are you feeling today?")
    mood = input("Enter your current mood (describe it briefly): ")
    
    scores = analyzer.polarity_scores(mood)
    if scores['compound'] >= 0.05:
        return 'happy'
    elif scores['compound'] <= -0.05:
        return 'sad'
    else:
        return 'neutral'
