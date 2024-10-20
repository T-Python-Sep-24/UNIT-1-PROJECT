# import local modules
from views import main_view as v
from controllers import main_controller as c

view = v.MainView()
controller = c.MainController(view)


while True:
    controller.show_menu()
    pick: int = input("Enter: ")
    print()

