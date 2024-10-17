import datetime
import json


class Workout():


    fileName='workouts.json'

    def __init__(self):

        self.workouts = []
        self.fileName = 'workouts.json'
        self.workout_type = ""
        self.workout_duration = ""
        self.workout_intensity = ""
        self.calories_burned = 0
        self.workout_date = ""
        self.workout_goals = ""

    def add_workout(self, workout_type, duration, intensity, calories_burned, workout_date):

        self.workout_type = workout_type
        self.workout_duration = duration
        self.workout_intensity = intensity
        self.calories_burned = calories_burned
        self.workout_date = workout_date
        self.workout_goals = []

        workout = {
            "type": self.workout_type,
            "duration": self.workout_duration,
            "intensity": self.workout_intensity,
            "calories_burned": self.calories_burned,
            "date": self.workout_date,
            "goals": []

        }
        self.workouts.append(workout)
        self.__save_to_file(self.fileName)
        print(" >> Workout added successfully ✅ ")

    def update_workout(self, workout_number, workout_attr, new_value):
        self.workouts[int(workout_number) - 1][workout_attr] = new_value
        self.__save_to_file(self.fileName)
        print("Workout information updated successfully ✅ ")

    def get_workouts(self):
        self.__load_from_file(self.fileName)
        self.formatOutput()


    def get_goals(self):
        return self.workout_goals


    def set_goals(self, workout_number:int, goals: list):
        self.__load_from_file(self.fileName)
        self.workouts[int(workout_number) - 1]['goals'] = goals
        self.__save_to_file(self.fileName)
        self.workout_goals = goals
        # todo update the list of goals for a specific workout
    def formatOutput(self):
        """
        Formats and prints a task from the to-do list.
        """
        print("-"*30)
        for i, w in enumerate(self.workouts, start=1):
            print(f"{i}. {w['type']} For ({w['duration']}) With {w['intensity']} Intensity, "
                  f"Burning {w['calories_burned']} Calories, Date:{w['date']} "
                  f"{"Your Goals:", w['goals'] if len(w['goals']) > 0 else "None"}")
        print("-"*30)

    def __save_to_file(self, fileName):
        """
        This method save the accounts data to the pickle file after it has been serialized
        :param fileName:
        :return:
        """
        try:
            with open(fileName, 'w') as f:
                json.dump(self.workouts, f, indent=4)
        except Exception as e:
            print(e)

    def __load_from_file(self, fileName):
        """
        This method loads all the accounts data from the pickle file and deserialize it
        :param fileName:
        :return: accounts
        """

        try:
            with open(fileName, 'r') as file:
                self.workouts = json.load(file)
                print(f"Loading Data ... ⏳")
                return self.workouts
        except Exception as e:
            print(f"Error loading from file The File might be Empty or {e} ⚠ ")
