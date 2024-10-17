
class Meal():

    def __init__(self, meal_name: str, meal_calories: float, meal_macronutrients: str, water_intake: float, meal_date:str):

        self.meal_name = meal_name
        self.meal_calories = meal_calories  # API is recommended
        self.meal_macronutrients = meal_macronutrients  # API is recommended
        self.water_intake = water_intake
        self.meal_date = meal_date

    def add_meal(self):
        pass
    def update_meal(self):
        pass
    def get_meals(self):
        pass
    def suggest_meals(self):
        # APIs are recommended
        pass
