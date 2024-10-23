#  lists and dictionaries to store questions and user responses.
questions = [
    {
        "question": "You enjoy social gatherings.",
        "options": ["Strongly Agree", "Agree", "Disagree", "Strongly Disagree"],
        "weights": [2, 1, -1, -2]  # Favoring Extroverts
    },
    {
        "question": "You prefer to plan things in advance rather than being spontaneous.",
        "options": ["Strongly Agree", "Agree", "Disagree", "Strongly Disagree"],
        "weights": [1, 2, -1, -2]  # Emphasizing Ambiverts
    },
    {
        "question": "You often feel overwhelmed in large groups.",
        "options": ["Strongly Agree", "Agree", "Disagree", "Strongly Disagree"],
        "weights": [-2, -1, 1, 2]  # Favoring Introverts
    },
    {
        "question": "You enjoy trying new experiences.",
        "options": ["Strongly Agree", "Agree", "Disagree", "Strongly Disagree"],
        "weights": [2, 1, -1, -2]  # Favoring Extroverts
    },
    {
        "question": "You prefer to work alone rather than in a team.",
        "options": ["Strongly Agree", "Agree", "Disagree", "Strongly Disagree"],
        "weights": [-2, -1, 1, 2]  # Favoring Introverts
    },
    {
        "question": "You tend to follow your heart over your head.",
        "options": ["Strongly Agree", "Agree", "Disagree", "Strongly Disagree"],
        "weights": [1, 2, -1, -2]  # Emphasizing Ambiverts
    },
    {
        "question": "You find it easy to make new friends.",
        "options": ["Strongly Agree", "Agree", "Disagree", "Strongly Disagree"],
        "weights": [2, 1, -1, -2]  # Favoring Extroverts
    },
    {
        "question": "You often feel anxious in unfamiliar situations.",
        "options": ["Strongly Agree", "Agree", "Disagree", "Strongly Disagree"],
        "weights": [-2, -1, 1, 2]  # Favoring Introverts
    },
    {
        "question": "You enjoy engaging in philosophical discussions.",
        "options": ["Strongly Agree", "Agree", "Disagree", "Strongly Disagree"],
        "weights": [1, 2, -1, -2]  # Emphasizing Ambiverts
    },
    {
        "question": "You value logic over emotions when making decisions.",
        "options": ["Strongly Agree", "Agree", "Disagree", "Strongly Disagree"],
        "weights": [1, 2, -1, -2]  # Emphasizing Ambiverts
    },
    {
        "question": "You prefer detailed plans over open-ended tasks.",
        "options": ["Strongly Agree", "Agree", "Disagree", "Strongly Disagree"],
        "weights": [1, 2, -1, -2]  # Emphasizing Ambiverts
    },
    {
        "question": "You enjoy helping others solve their problems.",
        "options": ["Strongly Agree", "Agree", "Disagree", "Strongly Disagree"],
        "weights": [2, 1, -1, -2]  # Favoring Extroverts
    },
    {
        "question": "You often take time to reflect on your feelings.",
        "options": ["Strongly Agree", "Agree", "Disagree", "Strongly Disagree"],
        "weights": [2, 1, -1, -2]  # Favoring Introverts
    },
    {
        "question": "You thrive in fast-paced environments.",
        "options": ["Strongly Agree", "Agree", "Disagree", "Strongly Disagree"],
        "weights": [2, 1, -1, -2]  # Favoring Extroverts
    },
    {
        "question": "You find it difficult to express your feelings.",
        "options": ["Strongly Agree", "Agree", "Disagree", "Strongly Disagree"],
        "weights": [-2, -1, 1, 2]  # Favoring Introverts
    },
]

emotional_intelligence_questions = [
    {
        "question": "I can easily recognize my own emotions.",
        "options": ["Strongly Agree", "Agree", "Disagree", "Strongly Disagree"],
        "weights": [2, 1, -1, -2]
    },
    {
        "question": "I often consider how my actions affect others' feelings.",
        "options": ["Strongly Agree", "Agree", "Disagree", "Strongly Disagree"],
        "weights": [2, 1, -1, -2]
    },
    {
        "question": "I find it easy to empathize with others.",
        "options": ["Strongly Agree", "Agree", "Disagree", "Strongly Disagree"],
        "weights": [2, 1, -1, -2]
    },
    {
        "question": "I manage my emotions well in stressful situations.",
        "options": ["Strongly Agree", "Agree", "Disagree", "Strongly Disagree"],
        "weights": [2, 1, -1, -2]
    },
    {
        "question": "I often reflect on my emotional responses.",
        "options": ["Strongly Agree", "Agree", "Disagree", "Strongly Disagree"],
        "weights": [2, 1, -1, -2]
    },
    {
        "question": "I find it hard to express my emotions to others.",
        "options": ["Strongly Agree", "Agree", "Disagree", "Strongly Disagree"],
        "weights": [-2, -1, 1, 2]
    },
    {
        "question": "I can easily tell when others are upset.",
        "options": ["Strongly Agree", "Agree", "Disagree", "Strongly Disagree"],
        "weights": [2, 1, -1, -2]
    },
    {
        "question": "I am comfortable discussing my feelings with others.",
        "options": ["Strongly Agree", "Agree", "Disagree", "Strongly Disagree"],
        "weights": [2, 1, -1, -2]
    },
    {
        "question": "I often seek feedback from others about my emotional responses.",
        "options": ["Strongly Agree", "Agree", "Disagree", "Strongly Disagree"],
        "weights": [2, 1, -1, -2]
    },
    {
        "question": "I try to understand different perspectives in conflicts.",
        "options": ["Strongly Agree", "Agree", "Disagree", "Strongly Disagree"],
        "weights": [2, 1, -1, -2]
    },
]

learning_style_questions = [
    {
        "question": "When learning new information, I prefer to:",
        "options": ["See visual aids (charts, graphs)", "Listen to explanations", "Engage in hands-on activities", "Read text"],
        "weights": [2, 1, -1, -2]
    },
    {
        "question": "I remember information better when I:",
        "options": ["Take notes during a lecture", "Discuss it with others", "Practice it myself", "Look at images or diagrams"],
        "weights": [2, 1, -1, -2]
    },
    {
        "question": "During a presentation, I pay more attention to:",
        "options": ["Visual elements (slides, videos)", "The speaker's tone and voice", "How I can physically engage with the topic", "Text details"],
        "weights": [2, 1, -1, -2]
    },
    {
        "question": "I prefer to learn through:",
        "options": ["Watching demonstrations", "Listening to lectures", "Participating in simulations", "Reading articles"],
        "weights": [2, 1, -1, -2]
    },
    {
        "question": "When studying, I find it helpful to:",
        "options": ["Use color-coded notes", "Listen to recorded lectures", "Use models or role-playing", "Read aloud to myself"],
        "weights": [2, 1, -1, -2]
    },
    {
        "question": "In class, I often:",
        "options": ["Doodle or sketch what I'm learning", "Take detailed notes by ear", "Manipulate objects or tools", "Highlight important text"],
        "weights": [2, 1, -1, -2]
    },
    {
        "question": "I find it easier to remember something if I:",
        "options": ["Can visualize it in my mind", "Can repeat it out loud", "Can relate it to a physical activity", "Can write it down"],
        "weights": [2, 1, -1, -2]
    },
    {
        "question": "I prefer learning environments that:",
        "options": ["Include visual displays", "Have discussions and dialogue", "Allow for hands-on practice", "Feature reading materials"],
        "weights": [2, 1, -1, -2]
    },
    {
        "question": "When I encounter a problem, I tend to:",
        "options": ["Draw a diagram to visualize it", "Talk it out with someone", "Try to solve it by doing", "Write down the steps"],
        "weights": [2, 1, -1, -2]
    },
    {
        "question": "I enjoy activities that involve:",
        "options": ["Art and design", "Listening to music or lectures", "Sports or physical tasks", "Reading and writing"],
        "weights": [2, 1, -1, -2]
    },
]

# functions for different tasks, such as displaying questions, calculating scores, and saving/loading results.
def display_question(q):
    print(q["question"])
    for i, option in enumerate(q["options"]):
        print(f"{i + 1}. {option}")

#if statements and loops to handle user input and quiz flow.
    for q in questions:
     display_question(q)
    answer = int(input("Select option (1-4): ")) - 1
    score += q["weights"][answer]


    