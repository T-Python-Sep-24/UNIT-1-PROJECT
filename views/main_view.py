import directory_tree

class MainView:
    def __init__(self):
        self.main_menu: str = (
            "Pick: \n"
            "1: to show tree structure of Images_Source folder\n"
            "2: to show tree structure of Images_Destination folder\n"
            "3: to orgnize images by year\n"
            "4: to orgnize images by month\n"
            "5: to exit"
        )

    def display_menu(self):
        print(self.main_menu)
        
    def display_tree(self, directory_path):
        directory_tree.display_tree(directory_path)
        input("")
    