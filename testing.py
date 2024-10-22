import os
import requests
from tqdm import tqdm
import time  # To simulate time delay for the progress bar

def calcCalories(query, weight, height, gender, age):

    # Nutritionix API credentials from .env file
    API_ID = os.getenv('Calories_API_ID')
    API_KEY = os.getenv('Calories_API_KEY')

    # The URL for the exercise endpoint
    url = "https://trackapi.nutritionix.com/v2/natural/exercise"

    # Headers with your API credentials
    headers = {
        'x-app-id': API_ID,
        'x-app-key': API_KEY,
        'Content-Type': 'application/json'
    }

    # Payload for the API request
    data = {
        "query": query,
        "gender": gender,
        "weight_kg": weight,  # weight in kilograms
        "height_cm": height,  # height in centimeters
        "age": age
    }

    # Start the progress bar and make the API call
    with tqdm(total=100, desc="Calculating calories", ncols=100) as progress:
        for i in range(90):
            time.sleep(0.03)
            progress.update(1)

        response = requests.post(url, headers=headers, json=data)  # Make the API call
        progress.update(10)

    if response.status_code == 200:
        exercise_data = response.json()
        if 'exercises' in exercise_data:
            nf_calories = exercise_data['exercises'][0]['nf_calories']
            calories_burned = nf_calories
            return nf_calories
        else:
            print("No exercises found in the response.")
    else:
        return f"Error: {response.status_code}, {response.text}"


print(calcCalories("run for 30 minutes", 70, 180, 'male', 23))