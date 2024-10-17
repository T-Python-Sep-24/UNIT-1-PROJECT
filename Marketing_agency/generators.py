import random
import faker


class DataGenerators:

    def __init__(self):
        self.data = []
        self.fake_data = faker.Faker()


    def generate_employees(self,number):
        for x in range(number):
            employee = {
                "name":self.fake_data.name(),
                "id" :self.fake_data.id(),
                "address": self.fake_data.address(),
                "email": self.fake_data.email(),
                "role": random.choice(["Project Manager","Marketing Specialist","Human resources","Product Manager"]),
                "salary":round(random.uniform(7000,45000),2)
            }
            self.data.append(employee)
            print(f"Genareted {number} employees profile")
    def generate_clints(self,number):
        for x in range(number):
            clients = {
                "name": random.choice(["Minister in Education","Minister in Culture","Minister in Hajj and Umrah","Minister of Health","Minister in Finance"]),
                "contact number": self.fake_data.phone_number(),
                "email":self.fake_data.email(),
                "address":self.fake_data.address(),
            }
            self.data.append(clients)
            print(f"Generated {number} Clients Profiles")


    def generate_products(self,number):
        pass

    def generate_transections(self, number):
        pass


