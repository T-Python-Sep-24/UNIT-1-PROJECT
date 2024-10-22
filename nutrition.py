import os
import time

import dotenv
import requests

import base
import suggestmeals
from tqdm import tqdm
from dotenv import load_dotenv
load_dotenv()


class Meal:

    fileName = 'user_data_files/meals.json'

    def __init__(self):
        """
        init / constructor
        """
        self.meals = []
        self.fileName = 'user_data_files/meals.json'
        self.meal_name = ""
        self.meal_calories = ""  # API is recommended
        self.meal_macronutrients = {}  # API is recommended
        self.water_intake = 0  # litre
        self.meal_date = ""

    def add_meal(self, meal_name, meal_calories, meal_macronutrients, water_intake, meal_date):
        """
        method to add meals data to files
        :param meal_name:
        :param meal_calories:
        :param meal_macronutrients:
        :param water_intake:
        :param meal_date:
        :return:
        """
        self.meal_name = meal_name
        self.meal_calories = meal_calories
        self.meal_macronutrients = meal_macronutrients
        self.water_intake = water_intake
        self.meal_date = meal_date

        meal = {
            'name': self.meal_name,
            'calories': self.meal_calories,
            'macronutrients': self.meal_macronutrients,
            'water': self.water_intake,
            'date': self.meal_date
        }

        # Append meal to the list once
        self.meals.append(meal)
        print(self.meals)
        # Save to file
        base.save_to_file(self.fileName, self.meals)
        print(" >> Meal added successfully ✅ ")

    def update_meal(self, meal_number, meal_attr, new_value):
        """
        this method update existing meals data and save to files
        :param meal_number:
        :param meal_attr:
        :param new_value:
        :return:
        """
        self.meals = base.load_from_file(self.fileName)
        self.meals[int(meal_number) - 1][meal_attr] = new_value
        base.save_to_file(self.fileName, self.meals)
        print("Workout information updated successfully ✅ ")

    def get_meals(self):
        """
        this method displays all meals in file
        :return:
        """
        self.meals = base.load_from_file(self.fileName)

        self.formatOutput()

    def calcFoodNutrients(self, query):

        # Nutritionix API credentials from .env file

        API_ID = os.getenv('Calories_API_ID')
        API_KEY = os.getenv('Calories_API_KEY')

        # The URL for the exercise endpoint
        url = "https://trackapi.nutritionix.com/v2/natural/nutrients"

        # Headers with your API credentials
        headers = {
            'x-app-id': '010f4a73',
            'x-app-key': '14fefbc8b1316e8e742142a40ab58f74',
            'Content-Type': 'application/json'
        }
        data = {
            "query": query,
        }
        with tqdm(total=100, desc="Calculating meal's Calories", ncols=100) as progress_par:
            for i in range(90):
                time.sleep(0.03)
                progress_par.update(1)

            response = requests.post(url, headers=headers, json=data)
            progress_par.update(10)

        if response.status_code == 200:

            foodsData = response.json()
            # print(json.dumps(foodsData, indent=4))
            calories = foodsData['foods'][0]['nf_calories']
            micronutrients = {
                'total_fats': foodsData['foods'][0]['nf_total_fat'],
                'saturated_fat': foodsData['foods'][0]['nf_saturated_fat'],
                'cholesterol': foodsData['foods'][0]['nf_cholesterol'],
                'sodium': foodsData['foods'][0]['nf_sodium'],
                'carbohydrate': foodsData['foods'][0]['nf_total_carbohydrate'],
                'dietary_fiber': foodsData['foods'][0]['nf_dietary_fiber'],
                'sugars': foodsData['foods'][0]['nf_sugars'],
                'protein': foodsData['foods'][0]['nf_protein'],
                'potassium': foodsData['foods'][0]['nf_potassium'],
            }
            return calories, micronutrients

        else:
            return f"Error: {response.status_code}, {response.text}"

    def suggest_meals(self,diet = None, maxCalories = 500, numOfSuggestions = 5, type = 'main course'):
        """
        this method uses the spoonacular api to suggest meals using default or customized inputs from the user
        :param diet:
        :param maxCalories:
        :param numOfSuggestions:
        :param type:
        :return:
        """
        # APIs are recommended
        suggestmeals.getSuggestions(diet, maxCalories, numOfSuggestions, type)

    def formatOutput(self):
        """
        Formats and prints a task from the to-do list.
        """
        print("-"*10 + " Meals Data " + "-"*10)
        for i, meal in enumerate(self.meals, start=1):
            print(f"{i}. {meal['name']} Contains {meal['calories']} Calories")
            print("Macronutrients: ")
            for j, (key, value) in enumerate(meal['macronutrients'].items(), 1):
                print(f"  {j}. {key.title()}: {value}")
            print(f"- Water Intake: {meal['water']} Liters")
            print(f"- Date: {meal['date']}")
            # print(f"{i}. {meal['name']} has ({meal['calories']}) And {meal['macronutrients']} macronutrients, "
            #       f"Your Water Intakes is {meal['water']} Liters, Date:{meal['date']}")
        print("-"*32)

    def remove_meal(self, num):
        self.meals = base.load_from_file(self.fileName)
        if len(self.meals) > 0:
            del self.meals[num - 1]
            base.save_to_file(self.fileName, self.meals)
            print("Meal is Deleted Successfully")
        else:
            print("You have no meals available")
