from views import main_view as m_v


# define OrgnizerView as subclass of MainView
class DeleterView(m_v.MainView):
    def __init__(self):
        super().__init__()
        self.delete_menu: str = (
            "Pick: \n"
            "1: to delete the contents of the Images_Source folder\n"
            "2: to delete the contents of the Images_Destination folder\n"
            "3: to abbort and go back to the main menu"
        )

    def show_delete_menu(self):
        print(self.delete_menu)

    def display_folder_is_empty(self):
        print("---- The folder is empty ----")
        input("")
