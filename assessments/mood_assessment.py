# assessments/mood_assessment.py

def assess_mood():
    """
    Function to assess the user's mood based on a questionnaire.
    Returns the mood score and corresponding mood description.
    """
    
    print("🧠 Let's assess your mood! Please answer the following questions on a scale of 1 to 10.")
    
    # Expanded list of questions to assess mood
    questions = [
        "How happy do you feel right now? (1-10)",
        "How stressed do you feel right now? (1-10, where 10 is extremely stressed)",
        "How energetic do you feel right now? (1-10)",
        "How relaxed do you feel right now? (1-10)",
        "How motivated do you feel today? (1-10)",
        "How connected do you feel to others? (1-10)",
        "How often do you feel overwhelmed? (1-10, where 10 is very often)",
        "How satisfied are you with your life right now? (1-10)",
        "How often do you feel anxious? (1-10, where 10 is very often)",
        "How much joy do you experience in your daily activities? (1-10)"
    ]
    
    total_score = 0
    for question in questions:
        while True:
            try:
                response = int(input(question + " "))
                if 1 <= response <= 10:
                    total_score += response
                    break
                else:
                    print("Please enter a number between 1 and 10.")
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 10.")
    
    # Calculate average (mood score)
    mood_score = total_score / len(questions)
    
    # Determine mood based on the score
    if mood_score <= 3:
        mood = "very low"
    elif mood_score <= 6:
        mood = "medium"
    else:
        mood = "high"
    
    return mood_score, mood