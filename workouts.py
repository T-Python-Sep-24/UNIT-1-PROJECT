import datetime

class Workout():

    def __init__(self, workout_type: str, workout_duration: int, workout_intensity: str, calories_burned: float, workout_data: str, workout_goals: str):

        self.workout_type = workout_type
        self.workout_duration = workout_duration
        self.workout_intensity = workout_intensity
        self.calories_burned = calories_burned
        self.workout_data = workout_data
        self.workout_goals = self.get_goals()

    def add_workout(self):

        pass
    def update_workout(self):
        pass
    def get_workouts(self):
        pass
    def get_goals(self):
        return self.workout_goals
    def set_goals(self):
        pass