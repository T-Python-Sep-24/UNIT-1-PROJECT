# recommendations/activities.py
def recommend_activity(score):
    """Provide recommendations based on the emotional score."""
    recommendations = {
        'low': [
            "🎬 Watch a comforting movie.",
            "📝 Journal your feelings.",
            "📞 Reach out to a friend.",
            "🌌 Stargaze or enjoy a sunset.",
            "🎵 Listen to soothing music.",
            "📚 Read a favorite book.",
            "🌿 Go for a nature walk.",
            "🛁 Take a relaxing bath.",
            "🐶 Spend time with a pet.",
            "🎨 Try painting or drawing.",
            "🍵 Make a cup of herbal tea.",
            "🧩 Solve a puzzle or brain teaser.",
            "🌧️ Write a letter to your future self.",
            "🎤 Sing your heart out to your favorite songs.",
            "🧘‍♂️ Try guided meditation.",
            "🌼 Plant some flowers or herbs."
        ],
        'medium': [
            "🎧 Listen to calming music.",
            "🌿 Take a short walk outdoors.",
            "🧘 Practice mindfulness.",
            "📚 Read an inspiring book.",
            "🎨 Try your hand at painting or drawing.",
            "🎤 Join a local singing group.",
            "🍳 Cook a new recipe.",
            "🏋️‍♀️ Do a light workout or yoga session.",
            "🌍 Attend a community event or workshop.",
            "📖 Start a new hobby or craft.",
            "🎉 Organize a get-together with friends.",
            "📝 Create a vision board.",
            "📅 Plan your week ahead.",
            "💪 Try a new sport or exercise class.",
            "📝 Write a gratitude list."
        ],
        'high': [
            "🎉 Celebrate with friends!",
            "🏃‍♀️ Engage in your favorite sport.",
            "🎨 Dive into a creative project.",
            "🌍 Plan a fun trip or outing.",
            "🥳 Host a game night with friends!",
            "🚴‍♂️ Go for a bike ride.",
            "🎈 Throw a small party for yourself.",
            "📸 Capture memories with photography.",
            "🧗‍♂️ Try an adventure sport like rock climbing.",
            "🎭 Attend a live performance or concert.",
            "💃 Take a dance class.",
            "🎬 Create your own short film.",
            "🧘‍♀️ Join a meditation or yoga retreat.",
            "📚 Volunteer at a local charity.",
            "🕺 Try a new social dance style.",
            "🌞 Go for a hike in nature."
        ]
    }

    if score < 4:
        return recommendations['low']
    elif score < 7:
        return recommendations['medium']
    else:
        return recommendations['high']
    