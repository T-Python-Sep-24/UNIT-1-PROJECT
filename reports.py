import base
import health_states
import nutrition
import workouts
from tabulate import tabulate


class Reports:

    def generate_daily_meals_report(self):

        mealsFile = nutrition.Meal().fileName
        meals_data = base.load_from_file(mealsFile)

        print("===============================")
        print("           Your Meals")
        print("===============================")
        for meal in meals_data:
            print("\nMeal Details")
            print("=============================")
            meal_details = [
                ["Name", meal['name']],
                ["Date", meal['date']],
                ["Calories", f"{meal['calories']} kcal"],
                ["Water", f"{meal['water']} glasses"]
            ]
            print(tabulate(meal_details, tablefmt="heavy_grid"))

            print("\nMacronutrients")
            print("=============================")
            macronutrients = [
                ["Total fats", meal['macronutrients']['total_fats']],
                ["Saturated fat", meal['macronutrients']['saturated_fat']],
                ["Cholesterol", meal['macronutrients']['cholesterol']],
                ["Sodium", meal['macronutrients']['sodium']],
                ["Carbohydrate", meal['macronutrients']['carbohydrate']],
                ["Dietary fiber", meal['macronutrients']['dietary_fiber']],
                ["Sugars", meal['macronutrients']['sugars']],
                ["Protein", meal['macronutrients']['protein']],
                ["Potassium", meal['macronutrients']['potassium']]
            ]
            print(tabulate(macronutrients, headers=["Nutrient", "Value"], tablefmt="heavy_grid"))
            print("-"*50)

    def generate_weekly_report(self):
        workout_data = base.load_from_file(workouts.Workout.fileName)
        # print(workout_data)

        for workout in workout_data:
            print("\nWorkout Details")
            print("=============================")
            workout_details = [
                ["Type", workout['type']],
                ["Duration", workout['duration']],
                ["Calories Burned", f"{workout['calories_burned']} kcal"],
                ["Date", workout['date']]
            ]
            print(tabulate(workout_details, tablefmt="heavy_grid"))

            # If there are goals, display them as well
            if workout['goals']:
                print("\nGoals")
                print("=============================")
                print(tabulate([[goal] for goal in workout['goals']], headers=["Goal"], tablefmt="heavy_grid"))
            else:
                print("\nNo goals for this workout.")
    def generate_monthly_report(self):
        health_states_data = base.load_from_file(health_states.Health_states().fileName)
        print("\nBody Measurements")
        print("=============================")
        for state in health_states_data:
        # Format data into table rows
            measurement_details = [
                ["Height", f"{state['height']} cm"],
                ["Weight", f"{state['weight']} kg"],
                ["BMI", f"{state['bmi']:.4f}"],
                ["Date", state['date']]
            ]

        # Display the table
            print(tabulate(measurement_details, tablefmt="heavy_grid"))


    # def format_report(self, data):
    #     if 'macronutrients' in data:
    #     # Nutrition data
    #         print("\nNutrition Information")
    #         print("=============================")
    #         nutrition_table = [
    #             ["Food", data['name']],
    #             ["Calories", data['calories']],
    #             ["Total Fats", f"{data['macronutrients']['total_fats']} g"],
    #             ["Saturated Fat", f"{data['macronutrients']['saturated_fat']} g"],
    #             ["Cholesterol", f"{data['macronutrients']['cholesterol']} mg"],
    #             ["Sodium", f"{data['macronutrients']['sodium']} mg"],
    #             ["Carbohydrate", f"{data['macronutrients']['carbohydrate']} g"],
    #             ["Dietary Fiber", f"{data['macronutrients']['dietary_fiber']} g"],
    #             ["Sugars", data['macronutrients']['sugars']],
    #             ["Protein", f"{data['macronutrients']['protein']} g"],
    #             ["Potassium", f"{data['macronutrients']['potassium']} mg"],
    #             ["Water", f"{data['water']} L"],
    #             ["Date", data['date']]
    #         ]
    #         print(tabulate(nutrition_table, tablefmt="heavy_grid"))
    #
    #     elif 'calories_burned' in data:
    #         # Workout data
    #         print("\nWorkout Details")
    #         print("=============================")
    #         workout_table = [
    #             ["Type", data['type']],
    #             ["Duration", data['duration']],
    #             ["Calories Burned", f"{data['calories_burned']} kcal"],
    #             ["Date", data['date']],
    #             ["Goals", ", ".join(data['goals']) if data['goals'] else "No goals set"]
    #         ]
    #         print(tabulate(workout_table, tablefmt="heavy_grid"))
    #
    #     elif 'bmi' in data:
    #         # Body measurements data
    #         print("\nBody Measurements")
    #         print("=============================")
    #         measurements_table = [
    #             ["Height", f"{data['height']} cm"],
    #             ["Weight", f"{data['weight']} kg"],
    #             ["BMI", f"{data['bmi']:.4f}"],
    #             ["Date", data['date']]
    #         ]
    #         print(tabulate(measurements_table, tablefmt="heavy_grid"))

    def display_report(self):
        pass
    def send_report_via_email(self, user_email):
        pass