import base
import suggestmeals


class Meal():

    fileName='meals.json'

    def __init__(self):
        """
        init / constructor
        """
        self.meals = []
        self.fileName = 'meals.json'
        self.meal_name = ""
        self.meal_calories = ""  # API is recommended
        self.meal_macronutrients = ""  # API is recommended
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
        # print("Coming Soon (; ")

    def formatOutput(self):
        """
        Formats and prints a task from the to-do list.
        """
        print("-"*30)
        for i, meal in enumerate(self.meals, start=1):
            print(f"{i}. {meal['name']} has ({meal['calories']}) And {meal['macronutrients']} macronutrients, "
                  f"Your Water Intakes is {meal['water']} Liters, Date:{meal['date']}")
        print("-"*30)