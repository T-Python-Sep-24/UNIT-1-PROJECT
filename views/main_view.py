import directory_tree


class MainView:
    def __init__(self):
        self.main_menu: str = (
            "Pick: \n"
            "1: to show tree structure of Images_Source folder\n"
            "2: to show tree structure of Images_Destination folder\n"
            "3: to orgnize images by year\n"
            "4: to orgnize images by month\n"
            "5: to orgnize images by face recognition\n"
            "6: to delete the contents of the images folder\n"
            "7: to exit\n"
        )

    def display_menu(self):
        print(self.main_menu)

    def display_thank_you(self):
        print("Thank you for using the Album orgnizer program, come back again soon")

    def display_wrong_input(self):
        print("---- Wrong input. Please try again ----")
        input("")
        
    def display_tree(self, directory_path):
        directory_tree.display_tree(directory_path)
        input("")
    
    def display_file_exist_error_msg(self, folder_name):
        print(f"---- You already have a {folder_name} inside the Images_Destination ----")

    def display_Exception_msg(self, e):
        print(f"---- Please contact admin and provide him with the error message: '{e}' ----")
        input("")

    def display_try_again_after_delete_dest(self):
        print(f"---- Please try again after deleting the contents of Images_Destination ----")
        input("")

    def display_try_again_after_put_in_src(self):
        print(f"---- Please try again after putting content in Images_Source ----")
        input("")
