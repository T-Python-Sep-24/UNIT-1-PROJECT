import requests

def getSuggestions():
    # Replace with your own API key from Spoonacular
    API_KEY = "47d8f549f16143e39ae9fc5106692b69"

    # API Endpoint for meal planning suggestions
    url = f"https://api.spoonacular.com/recipes/complexSearch"

    # Parameters for meal suggestions
    params = {
        'apiKey': API_KEY,
        'maxCalories': 500,  # Example: Max calories for the meal
        'number': 10,  # Number of meal suggestions to return
        'type': 'main course'  # Type of meal: 'main course', 'snack', etc.
    }

    # Send GET request to Spoonacular API
    response = requests.get(url, params=params)

    # Check if request was successful
    if response.status_code == 200:
        meal_data = response.json()

        # Print suggested meals
        if meal_data['results']:
            print(f"Suggested Meals ({len(meal_data['results'])} results):\n")
            for i, meal in enumerate(meal_data['results'], 1):
                title = meal.get('title', 'No title available')
                source_url = meal.get('sourceUrl', 'No source URL available')
                print(f"{i}. {title}")
                # print(f"   Recipe: {source_url}\n")
        else:
            print("No meal suggestions found.")
    else:
        print(f"Failed to retrieve meal suggestions. Status code: {response.status_code}")
