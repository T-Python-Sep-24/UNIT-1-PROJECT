
class Meal():

    fileName='meals.json'

    def __init__(self):
        self.meals = []
        self.meal_name = ""
        self.meal_calories = ""  # API is recommended
        self.meal_macronutrients = ""  # API is recommended
        self.water_intake = 0  # litre
        self.meal_date = ""

    def add_meal(self, meal_name, meal_calories, meal_macronutrients, water_intake, meal_date):

        self.meal_name = meal_name
        self.meal_calories = meal_calories
        self.meal_macronutrients = meal_macronutrients
        self.water_intake = water_intake
        self.meal_date = meal_date

        meal = {

            "name": meal_name,
            "calories": meal_calories,
            "macronutrients": meal_macronutrients,
            "water_intake": water_intake,
            "meal_date": meal_date

        }
        self.meals.append(meal)


    def update_meal(self):
        pass
    def get_meals(self):
        pass
    def suggest_meals(self):
        # APIs are recommended
        pass
