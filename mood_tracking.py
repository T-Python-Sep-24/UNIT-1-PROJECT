# mood_tracking.py

from datetime import datetime
import matplotlib.pyplot as plt

class MoodTracker:
    def __init__(self):
        self.entries = []

    def log_mood(self, mood):
        """Log mood with timestamp."""
        entry = {
            "mood": mood,
            "timestamp": datetime.now()
        }
        self.entries.append(entry)

    def display_mood_trends(self):
        """Display mood trends over time."""
        if not self.entries:
            print("No mood entries logged yet.")
            return

        moods = [entry['mood'] for entry in self.entries]
        timestamps = [entry['timestamp'] for entry in self.entries]

        # Convert moods to numeric values for plotting
        mood_values = [self.map_mood_to_value(mood) for mood in moods]

        plt.figure(figsize=(10, 5))
        plt.plot(timestamps, mood_values, marker='o')
        plt.title('Mood Tracking Over Time')
        plt.xlabel('Date')
        plt.ylabel('Mood')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def map_mood_to_value(self, mood):
        """Map mood strings to numeric values for plotting."""
        mood_map = {
            "happy": 2,
            "neutral": 1,
            "sad": 0
        }
        return mood_map.get(mood, 1)  # Default to neutral if mood not recognized