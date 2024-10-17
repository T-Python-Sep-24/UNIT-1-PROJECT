from User.Users import  Person

class Customer(Person):
    def __init__(self, user_name: str, email: str, password: str, phone_number: str) -> None:
        super().__init__(user_name, email, password, phone_number)
