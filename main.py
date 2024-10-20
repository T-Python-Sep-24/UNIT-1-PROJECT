import datetime

from colorama import Fore, Style

from reminders import Reminders
from workouts import Workout
from nutrition import Meal
from health_states import Health_states

# reminders menu

def remindersMenu():
    print(Fore.CYAN + "=" * 40)
    print("    (Workouts) Tracker")
    print("=" * 40 + Style.RESET_ALL)
    print("Please choose an option from the menu below:")
    print(Fore.GREEN + "1. Set Workout Reminder")  # done
    print("2. Set Meals Reminder") # done
    print("3. Set Health States Reminder") # done
    print("4. Get All Reminders")
    print(Fore.RED + "[Q/q]. Return to Main Menu" + Style.RESET_ALL)
    print("=" * 40)

def remindersTracking():

    # reminders_instance = Reminders()

    while True:

        remindersMenu()
        choice = input("Enter Your Choice: ")

        if choice == "1":
            # w = Workout()
            pass
        elif choice == "2":
            pass
        elif choice == "3":
            pass
        elif choice == "4":
            pass
        elif choice.lower() == "q":
            print("returning to main menu <<<")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 4 or q to return to main menu.")

# health states menu
def healthStatesMenu():

    print(Fore.CYAN + "=" * 40)
    print("    (Health States) Tracker")
    print("=" * 40 + Style.RESET_ALL)
    print("Please choose an option from the menu below:")
    print(Fore.GREEN + "1. Add Health States") # done
    print("2. Get Curring BMI") # done
    print("3. Display all Health States") # done
    # print("4. Track your Progress") # todo
    print(Fore.RED + "[Q/q]. Return to Main Menu" + Style.RESET_ALL)
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
    print("    (Nutrition) Tracker")
    print("=" * 40 + Style.RESET_ALL)
    print("Please choose an option from the menu below:")
    print(Fore.GREEN + "1. Add Meal")
    print("2. Update Meal data")
    print("3. Display Meals")
    print("4. Suggest meals")
    print(Fore.RED + "[Q/q] Return to Main Menu" + Style.RESET_ALL)
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

            elif isCutomized.lower() == 'n':
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
    print(Fore.GREEN + "1. Calculate Calories Burned")
    print("2. Add Workout")
    print("3. Update Workout data")
    print("4. Display Workouts / Goals")
    print("5. Goal Setting")
    print(Fore.RED + "[q/Q] Return to Main Menu" + Style.RESET_ALL)
    print("=" * 40)

def workoutTracking():

    workout_instance = Workout()
    while True:

        workoutTrackingMenu()
        choice = input("Enter Your choice: ")
        if choice == '1':

            activity = input("Enter workout Type: (e.g. Walking, Running, etc): ")
            duration = input("Enter workout duration (e.g. 30 minutes): ")
            query = activity + " " + duration
            weight = int(input("Enter Your Weight in kilograms (i.e 70): "))
            height = int(input("Enter Your Height in centimeters (i.e 175): "))
            age = int(input("Enter your age: "))
            gender = input("Enter your gender: ")

            nf_calories = workout_instance.calcCalories(query, weight, height, gender, age)

            w_date = datetime.date.today()

            print(f"You Burned {nf_calories} Calories ")
            c = input("Do you want to add workout to file [y/n] ? ")
            if c.lower() == 'y':

                workout_instance.add_workout(activity, duration, nf_calories, str(w_date))

            input(" >>> Press any Key to continue <<< ")
        elif choice == '2':
            # workout_type = input("Enter workout Type: (e.g. Walking, Running, etc): ").strip()
            # workout_duration = input("Enter workout duration followed with time unit: (e.g. 30m, 2h, 55s): ").strip()
            # calories_burned = float(input("Enter calories burned or skip to get the defaults: (e.g. 300): "))
            # workout_date = input("Enter The date (dd-mm-yyyy) or skip to get the current date (e.g. 25-11-2001): ")

            activity = input("Enter workout Type: (e.g. Walking, Running, etc): ")
            duration = input("Enter workout duration (e.g. 30 minutes): ")
            query = activity + " " + duration
            weight = int(input("Enter Your Weight in kilograms (i.e 70): "))
            height = int(input("Enter Your Height in centimeters (i.e 175): "))
            age = int(input("Enter your age: "))
            gender = input("Enter your gender: ")

            nf_calories = workout_instance.calcCalories(query, weight, height, gender, age)

            w_date = datetime.date.today()
            workout_instance.add_workout(activity, duration, nf_calories, str(w_date))

            input(" >>> Press any Key to continue <<< ")

        elif choice == '3':
            workout_instance.get_workouts()
            w_num = input("Enter the workout number to update: ")
            w_attribute = input("Enter the workout attribute that you want to update [type, duration, intensity, calories_burned, date, goals]: ")
            w_new_value = input("Enter the new attribute value to update: ")
            workout_instance.update_workout(w_num, w_attribute, w_new_value)
            input(" >>> Press any Key to continue <<< ")
        elif choice == '4':

            workout_instance.get_workouts()
            input(" >>> Press any Key to continue <<< ")

        elif choice == '5':

            workout_instance.get_workouts()
            if workout_instance.isWorkoutsAvailable():
                w_num = int(input("Enter workout Number to set its goals: "))
                duration_goal = input("Enter the duration goal: ")
                calories_burned_goal = input("Enter the calories to burn goal: ")
                workout_instance.set_goals(w_num, [duration_goal, calories_burned_goal])
            else:
                print("you have no workouts yet")
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
    print(Fore.YELLOW + "1. Track Workouts / Calories Burned")  # done
    print("2. Meal and Calorie Tracking")  # done
    print("3. Track health states and body mass index")  # done
    print("4. Set Reminders")  # todo set email reminders
    print("5. Generate Reports")  # todo generate reports
    print("6. Clear Data")  # todo resit program data
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
            #Todo Call the reminders management function
            remindersTracking()

        elif choice == '5':
            #Todo Call the report generation function
            pass
        elif choice == '6':
            #Todo Clear all files function
            pass
        elif choice.lower() == 'q':
            print("Exiting the Health and Fitness Tracker. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 8.")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An Error occurred : {e}")