
class Health_states():

    def __init__(self, weight: float, height: float, bmi: float, measurements: dict):

        self.weight = weight
        self.height = height
        self.bmi = bmi
        self.measurements = measurements

    def add_weight(self, weight):
        self.weight = weight
    def calc_bmi(self):
        bmi = self.weight * self.height ** 2
        pass
    def get_bmi(self):
        return self.bmi
        pass
    def get_measurements(self):
        pass
    def track_prgress(self):
        pass