import base

class Health_states():

    def __init__(self):

        self.health_states = []
        self.fileName = 'health_states.json'
        self.weight = 0
        self.height = 0
        self.measure_date = ""
        self.bmi = 0

    def add_health_states(self, weight, height, date):

        self.weight = weight
        self.height = height
        self.bmi = self.calc_bmi()
        self.date = date
        self.health_states = []
        new_measurement = {
            "height": height,
            "weight": weight,
            "bmi": self.calc_bmi(),
            "date": self.date

        }
        self.health_states.append(new_measurement)
        base.save_to_file(self.fileName, self.health_states)
        print("data saved successfully ")

    def calc_bmi(self, weight, height):
        bmi = weight / (height ** 2)
        return bmi
    def get_bmi(self):
        bmi = self.weight / (self.height ** 2)
        self.bmi = bmi
        return bmi
    def get_health_states(self):
        self.health_states = base.load_from_file(self.fileName)
        for i in self.health_states:
            print(i)
    def bmi_categorization(self, bmi):
        if bmi < 18.5:
            print("You are classified as Underweight, which may increase the RISK of developing health problems")
        elif 18.5 < bmi < 24.9:
            print("Nice, you are at the normal range of weight, we hope you keep it that way to avoid health problems")
        elif 25.0 < bmi < 29.9:
            print("You are classified as OVERWEIGHT, which may INCREASE the RISK of developing health problems")
            print("watch your weight, and maintain a healthier life style and workout")
        elif 30 < bmi < 34.9:
            print("You are classified as OBESE CLASS I, which may have HIGH RISK of developing health problems")
            print("Be careful, your at risk please consider visiting the Nutritionist and take regular health checks")
        elif 35 < bmi < 39.9:
            print("You are classified as OBESE CLASS II, which may have VERY HIGH RISK of developing health problems")
            print("Be careful, your at risk please consider visiting the Nutritionist and take regular health checks")
        elif bmi > 40:
            print("You are classified as OBESE CLASS III, which may have EXTREMELY HIGH RISK of developing health problems")
            print("Be careful, you're at risk please consider visiting the Nutritionist and take regular health checks")

    def track_progress(self):
        pass