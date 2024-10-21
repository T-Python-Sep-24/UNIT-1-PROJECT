import datetime
import json

from colorama import Fore, Style

import base
import health_states
import nutrition
import user_data
import workouts
from user_data import User
from workouts import Workout
from nutrition import Meal
from health_states import Health_states
from reports import Reports

# todo add waiting for api styling

user = User()
user1 = user_data.User()
# generate reports
def reportsMenu():

    print(Fore.CYAN + "=" * 40)
    print("    (Reports) Tracker")
    print("=" * 40 + Style.RESET_ALL)
    print("Please choose an option from the menu below:")
    print(Fore.GREEN + "1. Generate daily meals reports")
    print("2. Generate Weekly Workout reports")
    print("3. Generate Monthly progress reports")
    print("4. Send Complete Reports Via Email")
    print(Fore.RED + "[Q/q]. Return to Main Menu" + Style.RESET_ALL)
    print("=" * 40)

def reportsTracking():

    reports_instance = Reports()

    while True:

        reportsMenu()
        choice = input("Enter Your Choice: ")

        if choice == "1":
            reports_instance.generate_daily_meals_report()
            input(" >>> Press any Key to continue <<< ")
        elif choice == "2":
            reports_instance.generate_weekly_report()
            input(" >>> Press any Key to continue <<< ")
        elif choice == "3":
            reports_instance.generate_monthly_report()
            input(" >>> Press any Key to continue <<< ")
        elif choice == "4":

            email = user.get_email()
            isNotValid = user.validate_email(email)
            while True:
                if user.validate_email(email):
                    reports_instance.send_report_via_email(email)
                    print(f"Reports is sent to {email}")
                    break
                else:
                    print("Email is not valid")
                    email = input("Please Enter Your Valid Email: ")

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
    print(Fore.GREEN + "1. Add Health States")  # done
    print("2. Calculate Your Current BMI")  # done
    print("3. Display all Health States")  # done
    print("4. Remove Health State")  # done
    # print("4. Track your Progress") # Todo
    print(Fore.RED + "[Q/q]. Return to Main Menu" + Style.RESET_ALL)
    print("=" * 40)

def healthStatesTracking():

    health_states_instance = Health_states()

    while True:

        healthStatesMenu()
        choice = input("Enter Your Choice: ")

        if choice == "1":

            weight = float(input("Enter Your Weight: "))
            c = input("Do you want to Enter New Height and new Date [y/n] ? ")
            if c.lower() == 'n':
                height = user1.get_height()
                date = datetime.date.today()
            else:
                height = int(input("Enter New Height: "))
                date = input("Enter date")

            health_states_instance.add_health_states(weight, height, str(date))
            input(" >>> Press any Key to continue <<< ")

        elif choice == "2":

            # enter data
            # if not user1.get_weight():
            #     weight = float(input("Enter Your Weight: "))

            c = input("Do you want to use your recent weight and height [y] "
                      "otherwise add new [n] weight and height [y/n] ? ")

            if c.lower() == 'y':
                weight = user1.get_weight()
                height = user1.get_height()
            else:
                weight = int(input("Enter new Weight: "))
                height = int(input("Enter new Height: "))

            # calc bmi
            bmi = health_states_instance.calc_bmi(weight, height)
            cat = health_states_instance.bmi_categorization(bmi)

            print(f"Your BMI is {bmi} which is categorized as {cat}")

            # ask the user to save it or not
            saveState = input("Do you want to add this data to your file [y/n] ? ")
            if saveState.lower() == 'y':
                date = datetime.date.today()
                health_states_instance.add_health_states(weight, height, str(date))

            input(" >>> Press any Key to continue <<< ")

        elif choice == "3":
            health_states_instance.get_health_states()
            input(" >>> Press any Key to continue <<< ")

        elif choice == "4":
            health_states_instance.get_health_states()
            num = int(input("Enter state number to delete: "))
            health_states_instance.remove_state(num)
            input(" >>> Press any Key to continue <<< ")

        elif choice.lower() == "q":
            print("returning to main menu <<<")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 3 or q to return to main menu.")

# Nutrition's Menu
def nutritionsTrackingMenu():

    print(Fore.CYAN + "=" * 40)
    print("    (Nutrition) Tracker")
    print("=" * 40 + Style.RESET_ALL)
    print("Please choose an option from the menu below:")
    print(Fore.GREEN + "1. Query Meals")
    print("2. Update Meal data")
    print("3. Display Meals")
    print("4. Suggest meals")
    print("5. Remove Meal")
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
            quantity = input("Enter meal quantity in grams: ")
            query = quantity + " grams of " + meal_name
            meal_calories, meal_macronutrients = nutrition_instance.calcFoodNutrients(query)

            print("-"*35)
            print(f"{meal_name} calories and nutrients: ")
            print("-"*35)
            print(f"1. {meal_calories} Calories Per {quantity} Grams")

            for i, (key, value) in enumerate(meal_macronutrients.items(), start=2):

                print(f"{i}. {key.title()}: {value}")

            print("-"*35)
            c = input("Do you want to add this meal to your file [y/n] ? ")
            if c.lower() == 'y':

                water_intake = input("Enter your water intake in liters: ")
                meal_date = datetime.date.today()

                nutrition_instance.add_meal(meal_name, meal_calories, meal_macronutrients, water_intake, str(meal_date))

            input(" >>> Press any Key to continue <<< ")

        elif choice == '2':

            nutrition_instance.get_meals()
            m_num = input("Enter the meal number to update: ")
            m_attribute = input("Enter the meal attribute that you want to update [name, calories, macronutrients, water, date]: ")
            m_new_value = input("Enter the new attribute's value to update: ")  # todo update attr to update (CLI)
            nutrition_instance.update_meal(m_num, m_attribute, m_new_value)
            input(" >>> Press any Key to continue <<< ")

        elif choice == '3':
            # print all meals function
            nutrition_instance.get_meals()
            input(" >>> Press any Key to continue <<< ")

        elif choice == '4':

            isCutomized = input("Do you want a customized Suggestion [y/n] otherwise Random? ")
            if isCutomized.lower() == "y":
                # Todo Edit customization options (CLI)
                diet = input("Enter diet type [vegetarian, vegan, keto, paleo] or enter None: ")
                maxCalories = int(input("Enter maximum calories wanted in the meal: "))
                numOfSuggestions = int(input("Enter the Number of suggested meals you want: "))
                meal_type = input("Enter the meal type [main course, side dish, salad, "
                             "snack, soup, appetizer, dessert, drink, beverage]: ")
                nutrition_instance.suggest_meals(diet, maxCalories, numOfSuggestions, meal_type)

            elif isCutomized.lower() == 'n':
                nutrition_instance.suggest_meals()
            input(" >>> Press any Key to continue <<< ")

        elif choice == '5':

            nutrition_instance.get_meals()
            num = int(input("Enter Meal number to delete: "))
            nutrition_instance.remove_meal(num)

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
    print("6. Remove Workout")
    print(Fore.RED + "[q/Q] Return to Main Menu" + Style.RESET_ALL)
    print("=" * 40)

def workoutTracking():

    workout_instance = Workout()
    health_states_instance = Health_states()

    user_weight = user1.get_weight()

    while True:

        workoutTrackingMenu()
        choice = input("Enter Your choice: ")
        if choice == '1':

            activity = input("Enter workout Type: (e.g. Walking, Running, etc): ")
            duration = int(input("Enter workout duration in minutes(e.g. 30 ): "))
            query = activity + " " + str(duration) + "minutes"

            height = user1.get_height()
            weight = user1.get_weight()
            age = user1.get_age()
            gender = user1.get_gender()

            nf_calories = workout_instance.calcCalories(query, weight, height, gender, age)
            w_date = datetime.date.today()

            print(f"You Burned {nf_calories} Calories ")
            c = input("Do you want to add workout and health states to file [y/n] ? ")
            if c.lower() == 'y':

                workout_instance.add_workout(activity, duration, nf_calories, str(w_date))
                health_states_instance.add_health_states(weight, height, str(w_date))

            input(" >>> Press any Key to continue <<< ")
        elif choice == '2':
            # workout_type = input("Enter workout Type: (e.g. Walking, Running, etc): ").strip()
            # workout_duration = input("Enter workout duration followed with time unit: (e.g. 30m, 2h, 55s): ").strip()
            # calories_burned = float(input("Enter calories burned or skip to get the defaults: (e.g. 300): "))
            # workout_date = input("Enter The date (dd-mm-yyyy) or skip to get the current date (e.g. 25-11-2001): ")

            activity = input("Enter workout Type: (e.g. Walking, Running, etc): ")
            duration = input("Enter workout duration (e.g. 30 minutes): ")
            query = activity + " " + duration
            weight = user1.get_weight()
            height = user1.get_height()
            age = user1.get_age()
            gender = user1.get_gender()

            nf_calories = workout_instance.calcCalories(query, weight, height, gender, age)

            w_date = datetime.date.today()
            workout_instance.add_workout(activity, duration, nf_calories, str(w_date))

            input(" >>> Press any Key to continue <<< ")

        elif choice == '3':
            workout_instance.get_workouts()
            w_num = input("Enter the workout number to update: ")
            w_attribute = input("Enter the workout attribute that you want to update [type, duration, calories_burned, date, goals]: ")
            w_new_value = input("Enter the new attribute value to update: ")
            workout_instance.update_workout(w_num, w_attribute, w_new_value) # todo edit choosing attr to update (CLI)
            input(" >>> Press any Key to continue <<< ")

        elif choice == '4':

            workout_instance.get_workouts()
            input(" >>> Press any Key to continue <<< ")

        elif choice == '5':

            workout_instance.get_workouts()
            if workout_instance.isWorkoutsAvailable():
                w_num = int(input("Enter workout Number to set its goals: "))
                duration_goal = input("Enter the Duration goal: ")
                calories_burned_goal = input("Enter the Calories to burn goal: ")
                workout_instance.set_goals(w_num, [duration_goal, calories_burned_goal])
            else:
                print("you have no workouts yet")
            input(" >>> Press any Key to continue <<< ")

        elif choice == '6':
            workout_instance.get_workouts()
            num = int(input("Enter workout number to delete: "))
            workout_instance.remove_workout(num)

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
    print("4. Generate Reports")  # done
    print("5. Clear Data")  # todo resit program data
    print(Fore.RED + "[q/Q]. Exit" + Style.RESET_ALL)
    print("=" * 40)

def userAuth():
    """
    Authorize user, and collecting user information
    :return:
    """
    fileName = 'user_data_files/user.json'
    x = base.load_from_file(fileName)
    # print(x)
    if x is None:
        print("")
        print("-"*8 + " Welcome To " + Fore.MAGENTA + "FitTracker " + Style.RESET_ALL + "-"*8)
        print()
        print(Fore.BLUE+"> Please Register for New Account")
        print("~"*39)
        name = input("Enter Your name: ")
        email = input("Enter Your Email: ")

        age = int(input("Enter You age: "))
        gender = input("Enter your gender: ")
        weight = int(input("Enter your weight: "))
        height = int(input("Enter your height: "))

        user1.set_name(name)
        user1.set_age(age)
        user1.set_gender(gender)
        user1.set_height(height)
        user1.set_weight(weight)

        userAccount = {
            'username': name,
            'age': age,
            'gender': gender,
            'height': height,
            'weight': weight,
            'email': email,
            'emailIsValid': user1.validate_email(email)
        }

        base.save_to_file(fileName, userAccount)
        main()

    else:
        notAuthorized = True
        while notAuthorized:
            print("-"*8 + " Welcome To " + Fore.MAGENTA + "FitTracker " + Style.RESET_ALL + "-"*8)
            print(" >> Please Log in << ")

            name = input("Enter Your name: ")
            if name == x['username']:
                print(Fore.GREEN + "        welcome to FitTracker ")
                main()
                notAuthorized = False
            else:
                print(Fore.RED + "Wrong username !!")
                input("Press Enter to Try Again" + Style.RESET_ALL)

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
            input(" >>> Press any Key to continue <<< ")
        elif choice == '4':
            reportsTracking()
            input(" >>> Press any Key to continue <<< ")
        elif choice == '5':
            f1, f2, f3 = workouts.Workout.fileName, nutrition.Meal.fileName, health_states.Health_states.fileName
            base.clear_files(f1, f2, f3)

        elif choice.lower() == 'q':
            print(Fore.MAGENTA + "Exiting the Health and Fitness Tracker. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 8.")

if __name__ == "__main__":
    try:
        userAuth()
    except KeyboardInterrupt as e:
        print(Fore.LIGHTMAGENTA_EX + "GoodBye !!")
    except Exception as e:
        print(f"An Error occurred : {e}")