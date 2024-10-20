from views import main_view as v


class MainController:
    def __init__(self, main_view: v.MainView):
        self.view = main_view

    def show_menu(self):
        """ Show menu by calling display menu from MainView"""
        self.view.display_menu()
