import colorama

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

        self.welcome: str = "********** Welcome to Album Orgnizer Program! **********"
        self.border_w: str = "*" * len(self.welcome)
        self.border_m: str = "=" * len(self.welcome)
        self.border_f: str = "-" * len(self.welcome)
        self.border_s: str = "+" * len(self.welcome)
        
    def display_welcome(self):
        print(f"\n{self.border_w}\n{self.welcome}\n{self.border_w}\n")
        print(
            "The Album Organizer is designed to automate the\n"
            + "organization of image collections. based on user\n" 
            + "preferences. Helping you manage large photo collections\n" 
             )

    def display_menu(self):
        print(f"{self.border_m}\n{self.main_menu}{self.border_m}")

    def display_thank_you(self):
        print(self.border_w)
        print("* Thank you for using the Album orgnizer, see you soon *")
        print(self.border_w)

    def display_wrong_input(self):
        print(colorama.Fore.RED + self.border_f)
        print("------------- Wrong input. Please try again ------------")
        print(self.border_f + colorama.Fore.RESET)
        input("")
        
    def display_tree(self, directory_path):
        directory_tree.display_tree(directory_path)
        input("")
    
    def display_file_exist_error_msg(self, folder_name):
        print(colorama.Fore.RED + self.border_f)
        print(f"---- You already have a {folder_name} inside the Images_Destination ----")
        print(self.border_f + colorama.Fore.RESET)

    def display_Exception_msg(self, e):
        print(colorama.Fore.RED + self.border_f)
        print(f"---- Please contact admin and provide him with the error message: '{e}' ----")
        print(self.border_f + colorama.Fore.RESET)
        input("")

    # define metho in parent class so that subclasses can access it
    def display_try_again_after_delete_dest(self):
        print(colorama.Fore.RED + self.border_f)
        print(f"--- Failed: delete Images_Destination contents first ---")
        print(self.border_f + colorama.Fore.RESET)
        input("")

    # define metho in parent class so that subclasses can access it
    def display_try_again_after_put_in_src(self):
        print(colorama.Fore.RED + self.border_f)
        print(f"--- Failed: put content inside Images_Source first ---")
        print(self.border_f + colorama.Fore.RESET)
        input("")
