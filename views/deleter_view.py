import colorama

from views import main_view as m_v


# define OrgnizerView as subclass of MainView
class DeleterView(m_v.MainView):
    def __init__(self):
        super().__init__()
        self.delete_menu: str = (
            "Pick: \n"
            "1: to delete the contents of the Images_Source folder\n"
            "2: to delete the contents of the Images_Destination folder\n"
            "3: to abort and go back to the main menu\n"
        )

    def show_delete_menu(self):
        print(self.delete_menu)

    def display_folder_is_empty(self):
        print(colorama.Fore.RED + self.border_f)
        print("----------------- The folder is empty ------------------")
        print(self.border_f + colorama.Fore.RESET)
        input("")

    def display_image_dest_cleared(self):
        print(colorama.Fore.GREEN + self.border_s)
        print(f"+++ Images_Destination contents deleted successfully +++")
        print(self.border_s + colorama.Fore.RESET)
        input("")

    def display_image_src_cleared(self):
        print(colorama.Fore.GREEN + self.border_s)
        print(f"+++++ Images_Source contents deleted successfully ++++++")
        print(self.border_s + colorama.Fore.RESET)
        input("")
