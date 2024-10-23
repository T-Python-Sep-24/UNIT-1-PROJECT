# FitTtracker

A command-line app to help users log workouts, track meals, monitor progress, and achieve their health and fitness goals. This project allows users to stay on top of their fitness routines while maintaining an organized and data-driven approach to health tracking.

## Features

## Tracking User Data
### 1. Track Workouts and Goals
- Log different types of workouts (e.g., running, weightlifting, yoga) with details like duration, intensity, and calories burned.
- Set goals for specific exercises (e.g., running 5 miles, lifting 100 lbs).

### 2. Meals Calories And Nutrition Tracking
- Log daily meals with details such as calories, macronutrients (carbs, protein, fats), and water intake.
- Suggest healthy meal options based on calorie needs and dietary preferences (e.g., keto, vegan).

### 3. Daily/Weekly Health Stats
- Generate reports on weekly workout totals, calorie intake, and overall fitness progress.

### 4. Track Weight and Body Measurements
- Log daily/weekly weight, BMI.
- Show progress reports, using tables generated with `tabulate`.

### 5. Reports
- Use CLI-based tables or graphs to display trends and stats for workouts, weight changes, and diet tracking.

### 6. Export Data
- Export workout, nutrition, and health data to be sent to user via email .


---

## Code Organization

---

## Extensions And Libraries
This project is extended by integrating external APIs and Libraries such as:
- nutritionix: Calories Calculators from exercises and/or meals
- spoonacular: Nutrition and meals database
- Command Line Coloring and Animation (e.g., colorama, tabulate, tqdm)
The project is modular and organized to separate functionality, making it scalable and easy to maintain.

---

### Modules
- **`workouts.py`**: Manages exercise logs, workout tracking, and exercise goals.
- **`nutrition.py`**: Handles meal logging and calorie/macronutrient tracking.
- **`health_stats.py`**: Tracks user data such as weight, BMI, and body measurements.
- **`reports.py`**: Generates daily, weekly, and monthly fitness reports and trends.
- **`base.py`**: Contain static methods, such as load and save data to files
---

## Best Practices

- **Object-Oriented Programming**: Encapsulate user data (e.g., workouts, meals) and functionality (e.g., reminders) into classes and objects.
- **User Interaction**: Clean and responsive CLI interaction with proper validation and error handling.
- **Modularity**: Code is organized into manageable, scalable modules that can be extended with new features like API integration or mobile interfaces.
- **Separation of Concerns**: Each module is designed for specific functionalities (e.g., tracking workouts, meals, health stats) to ensure code reusability and maintainability.

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
   python app/main.py

---
