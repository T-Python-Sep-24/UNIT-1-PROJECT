from views import main_view as v


class MainController:
    def __init__(self, main_view: v.MainView):
        self.view = main_view

    def show_menu(self):
        """ Show menu by calling display menu from MainView"""
        self.view.display_menu()

    def display_orginal(self):
        """ Show tree structure of the Original_images folder """
        self.view.display_tree("./Original_images")
    
    def display_result(self):
        """ Show tree structure of the Result_images folder """
        self.view.display_tree("./Result_images")

