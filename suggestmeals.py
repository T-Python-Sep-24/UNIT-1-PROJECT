import random
import time

import requests
from dotenv import load_dotenv
import os
from tqdm import tqdm
load_dotenv()
def getSuggestions(diet = None, maxCalories = 500, numOfSuggestions = 5, type = 'main course'):
    # Replace with your own API key from Spoonacular
    API_KEY = os.getenv('spoonacularAPI_KEY')

    # API Endpoint for meal planning suggestions
    url = f"https://api.spoonacular.com/recipes/complexSearch"

    # Parameters for meal suggestions
    params = {
        'apiKey': API_KEY,
        'random': True,
        'diet': diet,  # Example: 'vegetarian', 'vegan', 'keto', 'paleo', etc.
        'maxCalories': maxCalories,  # Example: Max calories for the meal
        'number': numOfSuggestions,  # Number of meal suggestions to return
        'type': type  # Type of meal: 'main course', 'snack', etc.

    }
    with tqdm(total=100, desc="Preparing meals Suggestions", ncols=100) as progress_par:
        for i in range(90):
            time.sleep(0.03)
            progress_par.update(1)

        response = requests.get(url, params=params)
        progress_par.update(10)

    if response.status_code == 200:
        meal_data = response.json()

        # Print suggested meals
        if meal_data['results']:
            print(f"Suggested Meals found: {len(meal_data['results'])} \n")
            for i, meal in enumerate(meal_data['results'], 1):

                title = meal.get('title', 'No title available')
                source_url = meal.get('image', 'No image link available')

                print(f"{i}. {title}")
                print(f"   Image Link: {source_url}")
        else:
            print("No meal suggestions found.")
    else:
        print(f"Failed to retrieve meal suggestions. Status code: {response.status_code}")
