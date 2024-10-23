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
        print("\n---- The folder is empty ----")
        input("")

    def display_image_folder_cleared(self, folder_name):
        print(f"\n++++ The {folder_name} contents were deleted successfully ++++")
        input("")
