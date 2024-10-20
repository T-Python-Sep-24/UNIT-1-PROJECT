
class Services:
    def __init__(self, name, service_id, category):
        self.name = name
        self.service_id = service_id
        self.category = category

    # Function to create a method display
    def Display(self):
        print("Name:", self.name, "Service Id:", self.service_id, "Category:", self.category)