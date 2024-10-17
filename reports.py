class Reports():
    def __init__(self, workout_date: dict, nutrition_data: dict, health_stats:dict):
        self.workout_data = workout_date
        self.nutrition_data = nutrition_data
        self.health_stats = health_stats

    def generate_daily_report(self):
        pass
    def generate_weekly_report(self):
        pass
    def generate_monthly_report(self):
        pass
    def display_report(self):
        pass