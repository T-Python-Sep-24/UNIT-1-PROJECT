import colorama

from views import main_view as m_v


# define OrgnizerView as subclass of MainView
class OrgnizerView(m_v.MainView):
    def __init__(self):
        super().__init__()
        self.success: str = "++++++++ Your images were orgnized successfully ++++++++"
        self.failure: str = "---- Your images don't contain date in its file names ----"

    def display_orgniz_msg(self, orgnized_status: bool):
        if orgnized_status == True:
            print(colorama.Fore.GREEN + self.border_s)
            print(self.success)
            print(self.border_s + colorama.Fore.RESET)
            input("")
        else:
            print(colorama.Fore.RED + self.border_f)
            print(self.failure)
            print(self.border_f + colorama.Fore.RESET)
            input("")
