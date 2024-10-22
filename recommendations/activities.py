# recommendations/activities.py

from colorama import Fore

def recommend_activity(mood):
    activities = {
        'happy': ['🎉 Go for a run in nature', '🎶 Dance to your favorite song', '📖 Write down things you are grateful for'],
        'sad': ['🎬 Watch your favorite movie', '📝 Try journaling your thoughts', '📞 Talk to a friend or family member'],
        'anxious': ['🧘 Practice meditation', '🌬️ Do breathing exercises', '🧎‍ Stretch or do light yoga'],
        'angry': ['🥊 Punch a pillow or do a workout', '💨 Take deep breaths', '🚶 Go for a calming walk'],
        'excited': ['📅 Plan something exciting', '🎨 Channel energy into a hobby', '📲 Share your excitement with someone!'],
        'neutral': ['🎧 Listen to a podcast', '📚 Read a book', '🎨 Try learning something new']
    }
    return activities.get(mood, ['🛀 Relax and focus on self-care'])
