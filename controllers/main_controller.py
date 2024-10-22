from views import main_view as v
from models import orgnizer_model as m


class MainController:
    def __init__(self, main_view: v.MainView):
        self.view = main_view

    def show_menu(self):
        """ Show menu by calling display menu from MainView"""
        self.view.display_menu()

    def display_source(self):
        """ Show tree structure of the Images_Source folder """
        self.view.display_tree("./Images_Source")
    
    def display_destination(self):
        """ Show tree structure of the Images_Destination folder """
        self.view.display_tree("./Images_Destination")
