import time

from app import base, health_states, nutrition
import workouts
from tabulate import tabulate
import dotenv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from tqdm import tqdm
import os
dotenv.load_dotenv()


class Reports:

    def generate_daily_meals_report(self):

        mealsFile = nutrition.Meal().fileName
        meals_data = base.load_from_file(mealsFile)

        print("===============================")
        print("           Your Meals")
        print("===============================")
        for meal in meals_data:
            print("\nMeal Details")
            print("=============================")
            meal_details = [
                ["Name", meal['name']],
                ["Date", meal['date']],
                ["Calories", f"{meal['calories']} kcal"],
                ["Water", f"{meal['water']} Liters"]
            ]
            print(tabulate(meal_details, tablefmt="heavy_grid"))

            print("\nMacronutrients")
            print("=============================")
            macronutrients = [
                ["Total fats", meal['macronutrients']['total_fats']],
                ["Saturated fat", meal['macronutrients']['saturated_fat']],
                ["Cholesterol", meal['macronutrients']['cholesterol']],
                ["Sodium", meal['macronutrients']['sodium']],
                ["Carbohydrate", meal['macronutrients']['carbohydrate']],
                ["Dietary fiber", meal['macronutrients']['dietary_fiber']],
                ["Sugars", meal['macronutrients']['sugars']],
                ["Protein", meal['macronutrients']['protein']],
                ["Potassium", meal['macronutrients']['potassium']]
            ]
            print(tabulate(macronutrients, headers=["Nutrient", "Value"], tablefmt="heavy_grid"))
            print("-"*50)

    def generate_weekly_report(self):
        workout_data = base.load_from_file(workouts.Workout.fileName)
        # print(workout_data)

        for workout in workout_data:
            print("\nWorkout Details")
            print("=============================")
            workout_details = [
                ["Type", workout['type']],
                ["Duration", workout['duration']],
                ["Calories Burned", f"{workout['calories_burned']} kcal"],
                ["Date", workout['date']]
            ]
            print(tabulate(workout_details, tablefmt="heavy_grid"))

            # If there are goals, display them as well
            if workout['goals']:
                print("\nGoals")
                print("=============================")
                print(tabulate([[goal] for goal in workout['goals']], headers=["Goal"], tablefmt="heavy_grid"))
            else:
                print("\nNo goals for this workout.")

    def generate_monthly_report(self):
        health_states_data = base.load_from_file(health_states.Health_states().fileName)
        print("\nBody Measurements")
        print("=============================")

        if len(health_states_data) !=  None:

            for state in health_states_data:
            # Format data into table rows
                measurement_details = [
                    ["Height", f"{state['height']} cm"],
                    ["Weight", f"{state['weight']} kg"],
                    ["BMI", f"{state['bmi']:.4f}"],
                    ["Date", state['date']]
                ]

        # Display the table
                print(tabulate(measurement_details, tablefmt="heavy_grid"))

    def send_report_via_email(self, user_email):
        """
        method to send reminders and reports received from various classes to users
        :param user_email:
        :return:
        """
        sender_email = os.getenv('SENDER_EMAIL')  # Your Gmail address
        app_password = os.getenv('EMAIL_APP_PASSWORD')    # Your Gmail password or app-specific password

        # Recipient email
        receiver_email = user_email  # Recipient's email address example@gmail.com

        # Create the email message
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = receiver_email
        message['Subject'] = 'Health And Fitness Reports From Python Fitness Tracker'

        # Email body
        # body = 'Hello, this is a test email sent from Python with App Password!'

        meals_file = nutrition.Meal().fileName
        meals_data = base.load_from_file(meals_file)
        meals_table = []
        macronutrientsTable = []

        workoutsFile = workouts.Workout().fileName
        workout_data = base.load_from_file(workoutsFile)
        workoutsTable = []
        goals = []

        health_states_file = health_states.Health_states().fileName
        health_states_data = base.load_from_file(health_states_file)
        health_states_table = []

        total_calories = 0
        total_water_intake = 0
        # Initialize variables to store all the tables
        all_meals_table = ""
        all_workouts_table = ""
        all_health_states_table = ""

        # Process each meal and accumulate the HTML tables
        for meal in meals_data:
            total_calories += meal['calories']
            total_water_intake += meal['water']

            meal_details = [
                ["Meal Details"],
                ["Name", meal['name']],
                ["Date", meal['date']],
                ["Calories", f"{meal['calories']} kcal"],
                ["Water", f"{meal['water']} Liters"]
            ]
            meals_table = tabulate(meal_details, tablefmt="html")

            macronutrients = [
                ["Total fats", meal['macronutrients']['total_fats']],
                ["Saturated fat", meal['macronutrients']['saturated_fat']],
                ["Cholesterol", meal['macronutrients']['cholesterol']],
                ["Sodium", meal['macronutrients']['sodium']],
                ["Carbohydrate", meal['macronutrients']['carbohydrate']],
                ["Dietary fiber", meal['macronutrients']['dietary_fiber']],
                ["Sugars", meal['macronutrients']['sugars']],
                ["Protein", meal['macronutrients']['protein']],
                ["Potassium", meal['macronutrients']['potassium']]
            ]
            macronutrientsTable = tabulate(macronutrients, headers=["Nutrient", "Value"], tablefmt="html")

            # Accumulate the current meal tables
            all_meals_table += meals_table + macronutrientsTable + "<br>"

        # Process each workout and accumulate the HTML tables
        for workout in workout_data:
            workout_details = [
                ["Workout Details"],
                ["Type", workout['type']],
                ["Duration", workout['duration']],
                ["Calories Burned", f"{workout['calories_burned']} kcal"],
                ["Date", workout['date']]
            ]
            workoutsTable = tabulate(workout_details, tablefmt="html")

            # Handle goals for the workout
            if workout['goals']:
                goals = tabulate([[goal] for goal in workout['goals']], headers=["Goal"], tablefmt="html")
            else:
                goals = "\nNo goals for this workout."

            # Accumulate the current workout tables
            all_workouts_table += workoutsTable + "<br>" + goals + "<br>"

        # Process each health state and accumulate the HTML tables
        for state in health_states_data:
            measurement_details = [
                ["Height", f"{state['height']} cm"],
                ["Weight", f"{state['weight']} kg"],
                ["BMI", f"{state['bmi']:.4f}"],
                ["Date", state['date']]
            ]
            health_states_table = tabulate(measurement_details, tablefmt="html")

            # Accumulate the current health state tables
            all_health_states_table += health_states_table + "<br>"



# Now use your email sending logic to send `email_content` as the body


        html_content = f"""\
        <html>
            <head>
                <style>
                    table {{
                        width: 100%;
                        border-collapse: collapse;
                        margin: 20px 0;
                        font-family: Arial, sans-serif;
                        font-size: 14px;
                        width: 100%;
                        border-collapse: collapse;
                        margin-bottom: 20px;
                    }}
                    th, td {{
                        padding: 10px;
                      text-align: left;
                      border: 1px solid #ddd;
                    }}
                    table, th, td {{
                        border: 1px solid #dddddd;
                    }}
                
                    th, td {{
                        padding: 10px;
                        text-align: left;
                    }}
                
                    th {{
                        background-color: #f4f4f4;
                        font-weight: bold;
                    }}
                
                    tr:nth-child(even) {{
                        background-color: #f9f9f9;
                    }}
                
                    tr:hover {{
                        background-color: #f1f1f1;
                    }}
                
                    caption {{
                        font-size: 18px;
                        margin-bottom: 10px;
                        font-weight: bold;
                        text-align: left;
                    }}
                </style>
            </head>
            <body>
                <h1>Hello!</h1>
                <p>Hello, this is a Your Meals daily Report sent from Python.</p>
                <p><strong>Enjoy coding!</strong></p>
                <div>
                    <h2>Meal Information</h2>
                    {all_meals_table}
            
                    <h2>Workout Information</h2>
                    {all_workouts_table}
            
                    <h2>Health States</h2>
                    {all_health_states_table}
                </div>
                <a href="https://www.example.com">Click here to visit our website</a>
                <h3> THANK YOU ! </h3>
            </body>
        </html>
        """
        message.attach(MIMEText(html_content, 'html'))

        # Connect to Gmail's SMTP server and send the email
        try:
            # Set up the SMTP server
            smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
            smtp_server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            smtp_server.login(sender_email, app_password)  # Login with App Password
            with tqdm(total=100, desc="Sending Reports", ncols=100) as send_par:
                for i in range(90):
                    time.sleep(0.02)
                    send_par.update(1)
                # Send the email
                smtp_server.sendmail(sender_email, receiver_email, message.as_string())
                send_par.update(10)
            print('Email sent successfully!')

        except Exception as e:
            print(f"Error occurred: {e}")

        finally:
            # Close the server connection
            smtp_server.quit()

    # send_report_via_email("hamza.helal.d@gmail.com")
