import base

class Health_states():

    def __init__(self):
        """
        initializer / constructor
        """
        self.date = None
        self.health_states = []
        self.fileName = 'user_dataa_files/health_states.json'
        self.weight = 0
        self.height = 0
        self.measure_date = ""
        self.bmi = 0

    def add_health_states(self, weight, height, date):
        """
        method adds health states to file
        :param weight:
        :param height:
        :param date:
        :return:
        """
        self.weight = weight
        self.height = height
        self.bmi = self.get_bmi()
        self.date = date
        self.health_states = []
        new_measurement = {
            "height": height,
            "weight": weight,
            "bmi": self.get_bmi(),
            "date": self.date

        }
        self.health_states.append(new_measurement)
        base.save_to_file(self.fileName, self.health_states)
        print("data saved successfully ")

    def calc_bmi(self, weight, height):
        """
        method calculates and return the current bmi of the user
        :param weight:
        :param height:
        :return: bmi
        """
        bmi = weight / (height ** 2)
        return bmi
    def get_bmi(self):
        """
        this method calculates the user bmi taking the height and the wight from the current object
        :return:
        """
        bmi = self.weight / (self.height ** 2)
        self.bmi = bmi
        return bmi
    def get_health_states(self):
        """
        this method displays all records of the health states from files
        :return:
        """
        self.health_states = base.load_from_file(self.fileName)
        self.formatOutput()
    def bmi_categorization(self, bmi):
        """
        this method categorize user bmi and returns the appropriate msg
        :param bmi:
        :return:
        """
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
        """
        this method should be able to analyse all records of the health states and returns progress data
        :return:
        """
        pass
        # todo track progress
    def formatOutput(self):
        """
        Formats and prints a task from the to-do list.
        """
        print("-"*30)
        for i, state in enumerate(self.health_states, start=1):
            print(f"{i}. {state['height']}CM, ({state['weight']}) KG And {state['bmi']} body mass index, "
                  f"at {state['date']}")
        print("-"*30)