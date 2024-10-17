from colorama import Fore, Style

from workouts import Workout


def main_menu():
    print(Fore.CYAN + "=" * 40)
    print("    CLI Health and Fitness Tracker")
    print("=" * 40 + Style.RESET_ALL)
    print("Please choose an option from the menu below:")
    print(Fore.YELLOW + "1. Track Workouts")
    print("2. Meal and Calorie Tracking")
    print("3. View Daily/Weekly Health Stats")
    print("4. Goal Setting")
    print("5. Track Weight and Body Measurements")
    print("6. Set Reminders")
    print("7. Generate Reports")
    print("8. Exit" + Style.RESET_ALL)
    print("=" * 40)

def workoutTrackingMenu():

    print(Fore.CYAN + "=" * 40)
    print("    (Workouts) Tracker")
    print("=" * 40 + Style.RESET_ALL)
    print("Please choose an option from the menu below:")
    print(Fore.GREEN + "1. Add Workouts")
    print("2. Update Workout information")
    print("3. Display all Your Workouts / Goals")
    print("4. Goal Setting")
    print("5. Return to Main Menu" + Style.RESET_ALL)
    print("=" * 40)

def workoutTracking():

    workout_instance = Workout()
    while True:

        workoutTrackingMenu()
        choice = input("Enter Your choice: ")

        if choice == '1':
            workout_type = input("Enter workout Type: (e.g. running, weightlifting, etc): ").strip()
            workout_duration = input("Enter workout duration followed with time unit: (e.g. 30m, 2h, 55s): ").strip()
            workout_intensity = input("Enter workout intensity: [low, medium, high]: ").strip()
            calories_burned = float(input("Enter calories burned or skip to get the defaults: (e.g. 300): "))
            workout_date = input("Enter The date (dd-mm-yyyy) or skip to get the current date (e.g. 25-11-2001): ")
            # goalsC = input("Do you want to set up new workout goals ? otherwise we'll maintain the same previous goals [Y/N]: ")
            # if goalsC.lower() == "y":
            #     workout_goals = ""

            workout_instance.add_workout(workout_type, workout_duration, workout_intensity, calories_burned, workout_date)
            input(" >>> Press any Key to continue <<< ")

        elif choice == '2':
            workout_instance.get_workouts()
            w_num = input("Enter the workout number to update: ")
            w_attribute = input("Enter the workout attribute that you want to update [type, duration, intensity, calories_burned, date, goals]: ")
            w_new_value = input("Enter the new attribute value to update: ")
            workout_instance.update_workout(w_num, w_attribute, w_new_value)
        elif choice == '3':

            workout_instance.get_workouts()
            input(" >>> Press any Key to continue <<< ")

        elif choice == '4':

            workout_instance.get_workouts()
            w_num = int(input("Enter workout Number to set its goals: "))
            duration_goal = input("Enter the duration goal: ")
            calories_burned_goal = input("Enter the calories to burn goal: ")
            workout_instance.set_goals(w_num, [duration_goal, calories_burned_goal])

        elif choice == '5':
            break


def main():

    while True:
        main_menu()
        choice = input(">>> Enter your choice: ")

        if choice == '1':
            workoutTracking()
            input(" >>> Press any Key to continue <<< ")

        elif choice == '2':
            # Call the meal logging function
            pass
        elif choice == '3':
            # Call the health stats viewing function
            pass
        elif choice == '4':
            # Call the goal setting function
            pass
        elif choice == '5':
            # Call the weight and measurements tracking function
            pass
        elif choice == '6':
            # Call the reminders management function
            pass
        elif choice == '7':
            # Call the report generation function
            pass
        elif choice == '8':
            print("Exiting the Health and Fitness Tracker. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 8.")

if __name__ == "__main__":
    main()

# TODO keyboard gestures interact with menus if possible and useful

# import keyboard
#
# abc = True
#
# def run_func():
#     print('Hi, welcome!')
#     print('If you want to do this, press A or press B for doing that.')
#     while abc:
#         if keyboard.is_pressed('a'):
#             print('This function is run!')
#             abc = True
#
#         elif keyboard.is_pressed('b'):
#             print('That function is run!')
#             abc = True
#
# print('To start press S')
# while abc:
#     if keyboard.is_pressed('S'):
#         run_func()
#     abc = True