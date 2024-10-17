class PasswordError(Exception):
    def __init__(self, message) -> None:
        self.message=message
        super().__init__(self.message)

class EmailError(Exception):
    def __init__(self, message) -> None:
        self.message=message
        super().__init__(self.message)

class PhoneNumberError(Exception):
    def __init__(self,message) -> None:
        self.message=message
        super().__init__(self.message)
