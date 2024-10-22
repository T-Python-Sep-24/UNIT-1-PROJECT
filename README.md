# FitTracker

A command-line app to help users log workouts, track meals, monitor progress, and achieve their health and fitness goals. This project allows users to stay on top of their fitness routines while maintaining an organized and data-driven approach to health tracking.

## Features

### 1. Track Workouts
- Log different types of workouts (e.g., running, weightlifting, yoga) with details like duration, intensity, and calories burned.
- Set goals for specific exercises (e.g., running 5 miles, lifting 100 lbs).

### 2. Meal and Calorie Tracking
- Log daily meals with details such as calories, macronutrients (carbs, protein, fats), and water intake.
- Suggest healthy meal options based on calorie needs and dietary preferences (e.g., keto, vegan).

### 3. Daily/Weekly Health Stats
- Generate reports on weekly workout totals, calorie intake, and overall fitness progress.

### 4. Goal Setting
- Set fitness goals (e.g., lose 5 kg in 3 months, run a 10K race).

### 5. Track Weight and Body Measurements
- Log daily/weekly weight, BMI.
- Show progress reports, using tables generated with `tabulate`.


### 6. Export Data
- Export workout, nutrition, and health data to CSV or JSON formats for external analysis or send email reports to user.

### 7. Reports
- Use CLI-based tables or graphs to display trends and stats for workouts, weight changes, and diet tracking.


---

## Code Organization

The project is modular and organized to separate functionality, making it scalable and easy to maintain.

### Modules
- **`workouts.py`**: Manages exercise logs, workout tracking, and exercise goals.
- **`nutrition.py`**: Handles meal logging and calorie/macronutrient tracking.
- **`health_stats.py`**: Tracks user data such as weight, BMI, and body measurements.
- **`reports.py`**: Generates daily, weekly, and monthly fitness reports and trends.

---

## Best Practices

- **Object-Oriented Programming**: Encapsulate user data (e.g., workouts, meals) and functionality (e.g., reminders) into classes and objects.
- **Separation of Concerns**: Each module is designed for specific functionalities (e.g., tracking workouts, meals, health stats) to ensure code reusability and maintainability.
- **User Interaction**: Clean and responsive CLI interaction with proper validation and error handling.
- **Modularity**: Code is organized into manageable, scalable modules that can be extended with new features like API integration or mobile interfaces.

---

## Extensions And Libraries
This project is extended by integrating external APIs and Libraries such as:
- nutritionix: Calories Calculators from exercises and/or meals
- spoonacular: Nutrition and meals database
- Command Line Coloring and Animation (e.g., colorama, tabulate, tqdm)


---

## Installation and Setup

1. Clone this repository:
   ```bash
    git clone https://github.com/HmzhDubh/UNIT-1-PROJECT.git

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt

3. Run the Tracker:
   ```bash
   python main.py

---
