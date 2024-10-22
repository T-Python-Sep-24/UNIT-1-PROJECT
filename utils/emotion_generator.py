# utils/emotion_generator.py
import nltk
from nltk.corpus import wordnet

nltk.download('wordnet')

def generate_emotions(mood):
    """Generate related emotions based on the current mood."""
    synonyms = set()
    emotion_dict = {
        'happy': ['joyful', 'content', 'excited', 'ecstatic', 'cheerful', 'elated', 'optimistic', 'satisfied'],
        'sad': ['downcast', 'sorrowful', 'depressed', 'melancholy', 'blue', 'gloomy', 'disheartened', 'despondent'],
        'neutral': ['indifferent', 'apathetic', 'dispassionate', 'unmoved', 'average', 'complacent', 'unenthusiastic'],
        'anxious': ['worried', 'nervous', 'restless', 'tense', 'uneasy', 'apprehensive', 'jittery', 'on edge'],
        'angry': ['irritated', 'furious', 'enraged', 'frustrated', 'indignant', 'exasperated', 'fuming', 'seething'],
        'excited': ['thrilled', 'elated', 'animated', 'eager', 'enthusiastic', 'overjoyed', 'fired up', 'invigorated'],
        'bored': ['disinterested', 'weary', 'jaded', 'listless', 'uninspired', 'fatigued', 'tired'],
        'confused': ['bewildered', 'perplexed', 'uncertain', 'disoriented', 'flustered', 'baffled', 'lost'],
        'hopeful': ['optimistic', 'encouraged', 'promising', 'confident', 'assured', 'bright', 'buoyant'],
        'grateful': ['thankful', 'appreciative', 'indebted', 'obliged', 'contented', 'satisfied']
    }

    if mood in emotion_dict:
        synonyms.update(emotion_dict[mood])
    else:
        for syn in wordnet.synsets(mood):
            for lemma in syn.lemmas():
                synonyms.add(lemma.name())  # Gather synonyms

    return list(synonyms) if synonyms else [mood]