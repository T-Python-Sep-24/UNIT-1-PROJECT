class Orgnizer_view:
    def __init__(self):
        self.success: str = "++++ Your images were orgnized successfully ++++"
        self.failure: str = "---- Your images don't contain date in its file names ----"

    def display_orgniz_msg(self, orgnized_status: bool):
        if orgnized_status == True:
            print(self.success)
            input("")
        else:
            print(self.failure)
            input("")
