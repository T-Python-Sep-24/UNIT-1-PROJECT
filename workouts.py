
from dotenv import load_dotenv
import base
import os
import requests
import json
# Load secrets from dotenv
load_dotenv()


class Workout:

    fileName = 'workouts.json'

    def __init__(self):
        """
        initializer / constructor
        """

        self.workouts = []
        self.fileName = 'workouts.json'
        self.workout_type = ""
        self.workout_duration = ""
        self.calories_burned = 0
        self.workout_date = ""
        self.workout_goals = ""

    def add_workout(self, workout_type, duration, calories_burned, workout_date):
        """
        this method if to add new workout data
        :param workout_type:
        :param duration:
        :param calories_burned:
        :param workout_date:
        :return:
        """
        self.workout_type = workout_type
        self.workout_duration = duration
        self.calories_burned = calories_burned
        self.workout_date = workout_date
        self.workout_goals = []

        workout = {
            "type": self.workout_type,
            "duration": self.workout_duration,
            "calories_burned": self.calories_burned,
            "date": self.workout_date,
            "goals": []

        }
        self.workouts.append(workout)
        base.save_to_file(self.fileName, self.workouts)
        print(" >> Workout added successfully ✅ ")

    def update_workout(self, workout_number, workout_attr, new_value):
        """
        this method is to update the exiting workouts data
        :param workout_number:
        :param workout_attr:
        :param new_value:
        :return:
        """
        if self.isWorkoutsAvailable():
            self.workouts = base.load_from_file(self.fileName)
            self.workouts[int(workout_number) - 1][workout_attr] = new_value
            base.save_to_file(self.fileName, self.workouts)
            print("Workout information updated successfully ✅ ")
        else:
            print("you have no workouts yet")

    def get_workouts(self):
        """
        this method displays all existing workouts
        :return:
        """
        self.workouts = base.load_from_file(self.fileName)
        if self.isWorkoutsAvailable:
            self.formatOutput()
        else:
            print("You don't have any workouts available yet")

    def set_goals(self, workout_number: int, goals: list):
        """
        method to set goals of the workouts and add updated workouts data to file
        :param workout_number:
        :param goals:
        :return:
        """

        self.workouts = base.load_from_file(self.fileName)
        if self.isWorkoutsAvailable():
            self.workouts[int(workout_number) - 1]['goals'] = goals
            base.save_to_file(self.fileName, self.workouts)
            self.workout_goals = goals
            print("Goals Updated Successfully ✅ ")
        else:
            print("You can't set goals until you have a workout available")

    def formatOutput(self):
        """
        Formats and prints a task from the to-do list.
        """
        print("-"*30)
        if self.isWorkoutsAvailable():
            for i, workout in enumerate(self.workouts, start=1):
                print(f"{i}. {workout['type']} For ({workout['duration']}), "
                      f"Burning {workout['calories_burned']} Calories, Date:{workout['date']} "
                      f"{"Your Goals:", workout['goals'] if len(workout['goals']) > 0 else "None"}")
            print("-"*30)
        else:
            print("you have no workouts yet")

    def calcCalories(self, query, weight, height, gender, age):

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

        data = {
            "query": query,
            "gender": gender,
            "weight_kg": weight,  # weight in kilograms
            "height_cm": height,  # height in centimeters
            "age": age
        }

        response = requests.post(url, headers=headers, json=data)

        if response.status_code == 200:

            exercise_data = response.json()
            if 'exercises' in exercise_data:
                nf_calories = exercise_data['exercises'][0]['nf_calories']
                self.calories_burned = nf_calories
                # print(f"Calories burned: {nf_calories}")
                return  nf_calories
            else:
                print("No exercises found in the response.")

            # print(json.dumps(exercise_data, indent=4))
        else:
            return f"Error: {response.status_code}, {response.text}"


    def isWorkoutsAvailable(self):
        if self.workouts is None:
            return False
        else:
            return True