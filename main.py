from colorama import Fore, Style

from workouts import Workout
from nutrition import Meal
from health_states import Health_states


# health states menu
def healthStatesMenu():

    print(Fore.CYAN + "=" * 40)
    print("    (Workouts) Tracker")
    print("=" * 40 + Style.RESET_ALL)
    print("Please choose an option from the menu below:")
    print(Fore.GREEN + "1. Add Health States") # done
    print("2. Get Curring BMI") # done
    print("3. Display all Health States") # done
    # print("4. Track your Progress") # todo
    print("[Q/q]. Return to Main Menu" + Style.RESET_ALL)
    print("=" * 40)


def healthStatesTracking():

    health_states_instance = Health_states()

    while True:

        healthStatesMenu()
        choice = input("Enter Your Choice: ")

        if choice == "1":
            weight = float(input("Enter Your Weight: "))
            height = float(input("Enter Your Height: "))
            date = input("Enter measurement date: ")

            health_states_instance.add_health_states(weight, height, date)
            input(" >>> Press any Key to continue <<< ")

        elif choice == "2":
            if health_states_instance.get_bmi() == 0:

                # enter data
                weight = float(input("Enter your weight in (kg ie. 65): "))
                height = float(input("Enter your Height in (meters ie. 1.66): "))

                #calc bmi
                bmi = health_states_instance.calc_bmi(weight, height)
                cat = health_states_instance.bmi_categorization(bmi)
                print(f"Your BMI is {bmi} which is categorized as {cat}")

                # ask the user to save it or not
                saveOrnot = input("Do you want to add this data to your file [y/n] ? ")
                if saveOrnot.lower() == 'y':
                    date = input("please Enter date: ")
                    health_states_instance.add_health_states(weight, height, date)

                # get bmi
                # bmi = health_states_instance.calc_bmi()
                # cat = health_states_instance.bmi_categorization(bmi)
                # print(f"Your BMI is {bmi} which is categorized as {cat}")
            else:
                bmi = health_states_instance.get_bmi()
                cat = health_states_instance.bmi_categorization(bmi)
                print(f"Your BMI is {bmi} which is categorized as {cat}")

            input(" >>> Press any Key to continue <<< ")

        elif choice == "3":
            health_states_instance.get_health_states()
            input(" >>> Press any Key to continue <<< ")

        elif choice.lower() == "q":
            print("returning to main menu <<<")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 4 or q to return to main menu.")


# Nutrition's Menu
def nutritionsTrackingMenu():
    print(Fore.CYAN + "=" * 40)
    print("    (Workouts) Tracker")
    print("=" * 40 + Style.RESET_ALL)
    print("Please choose an option from the menu below:")
    print(Fore.GREEN + "1. Add Meal")
    print("2. Update Meal information")
    print("3. Display all Meals")
    print("4. Suggest meals")
    print("5. Return to Main Menu" + Style.RESET_ALL)
    print("=" * 40)

def nutritionTracking():

    nutrition_instance = Meal()

    while True:

        nutritionsTrackingMenu()
        choice = input("Enter Your choice: ")

        if choice == '1':
            # add meal function
            meal_name = input("Enter the meal name: ")
            meal_calories = input("Enter the calories of the meal: ")  # API is recommended
            meal_macronutrients = input("Enter meal macronutrients: ")  # API is recommended
            water_intake = input("Enter your water intake in liters: ")
            meal_date = input("Enter the date of the meal or skip for today's date: ")
            nutrition_instance.add_meal(meal_name, meal_calories, meal_macronutrients, water_intake, meal_date)
            input(" >>> Press any Key to continue <<< ")

        elif choice == '2':

            nutrition_instance.get_meals()
            m_num = input("Enter the meal number to update: ")
            m_attribute = input("Enter the meal attribute that you want to update [name, calories, macronutrients, water, date]: ")
            m_new_value = input("Enter the new attribute's value to update: ")
            nutrition_instance.update_meal(m_num, m_attribute, m_new_value)
            input(" >>> Press any Key to continue <<< ")

        elif choice == '3':
            # print all meals function
            nutrition_instance.get_meals()
            input(" >>> Press any Key to continue <<< ")

        elif choice == '4':

            isCutomized = input("Do you want a customized Suggestion [y/n] otherwise Random? ")
            if isCutomized.lower() == "y":

                diet = input("Enter diet type [vegetarian, vegan, keto, paleo] or enter None: ")
                maxCalories = int(input("Enter maximum calories wanted in the meal: "))
                numOfSuggestions = int(input("Enter the Number of suggested meals you want: "))
                type = input("Enter the meal type [main course, side dish, salad, snack, soup, appetizer, dessert, drink, beverage]: ")
                nutrition_instance.suggest_meals(diet, maxCalories, numOfSuggestions, type)

            else:
                nutrition_instance.suggest_meals()
            input(" >>> Press any Key to continue <<< ")

        elif choice.lower() == 'q':
            print("Returning to the main menu <<<")
            break

        else:
            print("Invalid choice! Please enter a number between 1 and 4 or q to return to main menu.")

# workout Menu
def workoutTrackingMenu():

    print(Fore.CYAN + "=" * 40)
    print("    (Workouts) Tracker")
    print("=" * 40 + Style.RESET_ALL)
    print("Please choose an option from the menu below:")
    print(Fore.GREEN + "1. Add Workouts")
    print("2. Update Workout information")
    print("3. Display all Your Workouts / Goals")
    print("4. Goal Setting")
    print(Fore.RED + "[q/Q] Return to Main Menu" + Style.RESET_ALL)
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
            input(" >>> Press any Key to continue <<< ")
        elif choice == '3':

            workout_instance.get_workouts()
            input(" >>> Press any Key to continue <<< ")

        elif choice == '4':

            workout_instance.get_workouts()
            w_num = int(input("Enter workout Number to set its goals: "))
            duration_goal = input("Enter the duration goal: ")
            calories_burned_goal = input("Enter the calories to burn goal: ")
            workout_instance.set_goals(w_num, [duration_goal, calories_burned_goal])
            input(" >>> Press any Key to continue <<< ")

        elif choice.lower() == 'q':
            print("Returning to the main menu >>>")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 4 or q to return to main menu.")

# Main menu
def main_menu():
    print(Fore.CYAN + "=" * 40)
    print("    CLI Health and Fitness Tracker")
    print("=" * 40 + Style.RESET_ALL)
    print("Please choose an option from the menu below:")
    print(Fore.YELLOW + "1. Track Workouts")  # done
    print("2. Meal and Calorie Tracking")  # done
    print("3. Track health states and body mass index")  # done
    print("5. Set Reminders")
    print("6. Generate Reports")
    print(Fore.RED + "[q/Q]. Exit" + Style.RESET_ALL)
    print("=" * 40)

def main():

    while True:
        main_menu()
        choice = input(">>> Enter your choice: ")

        if choice == '1':
            workoutTracking()
            input(" >>> Press any Key to continue <<< ")

        elif choice == '2':
            nutritionTracking()
            input(" >>> Press any Key to continue <<< ")
        elif choice == '3':
            healthStatesTracking()

        elif choice == '4':
            #Todo Call the goal setting function
            pass
        elif choice == '4':
            #Todo Call the weight and measurements tracking function
            pass
        elif choice == '5':
            #Todo Call the reminders management function
            pass
        elif choice == '6':
            #Todo Call the report generation function
            pass
        elif choice.lower() == 'q':
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