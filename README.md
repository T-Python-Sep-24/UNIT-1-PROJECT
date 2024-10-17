# CLI Health and Fitness Tracker

A command-line tool to help users log workouts, track meals, monitor progress, and achieve their health and fitness goals. This project allows users to stay on top of their fitness routines while maintaining an organized and data-driven approach to health tracking.

## Features

### 1. Track Workouts
- Log different types of workouts (e.g., running, weightlifting, yoga) with details like duration, intensity, and calories burned.
- Set goals for specific exercises (e.g., running 5 miles, lifting 100 lbs).

### 2. Meal and Calorie Tracking
- Log daily meals with details such as calories, macronutrients (carbs, protein, fats), and water intake.
- **Optional**: Suggest healthy meal options based on calorie needs and dietary preferences (e.g., keto, vegan).

### 3. Daily/Weekly Health Stats
- Generate reports on weekly workout totals, calorie intake, and overall fitness progress.
- Compare current stats with previous weeks to show improvement.

### 4. Goal Setting
- Set fitness goals (e.g., lose 5 kg in 3 months, run a 10K race).
- Track progress towards weight loss, muscle gain, or endurance goals.
- Alert users when they’re close to reaching a goal or have missed their targets.

### 5. Track Weight and Body Measurements
- Log daily/weekly weight, BMI, and other body measurements (e.g., waist, chest, arms).
- Show progress visually, using text-based graphs or graphs generated with `matplotlib`.

### 6. Reminders
- Set reminders to drink water, complete workouts, or log meals.
- Users can customize reminders based on their fitness routine and goals.

### 7. Export Data
- Export workout, nutrition, and health data to CSV or JSON formats for external analysis or sharing with a trainer or doctor.

### 8. Reports and Graphs
- Use CLI-based tables or graphs to display trends and stats for workouts, weight changes, and diet tracking.
- Integrate libraries like `matplotlib` for more advanced visualization.

---

## Code Organization

The project is modular and organized to separate functionality, making it scalable and easy to maintain.

### Modules
- **`workouts.py`**: Manages exercise logs, workout tracking, and exercise goals.
- **`nutrition.py`**: Handles meal logging and calorie/macronutrient tracking.
- **`health_stats.py`**: Tracks user data such as weight, BMI, and body measurements.
- **`reminders.py`**: Manages fitness reminders for workouts, meals, water intake, and more.
- **`reports.py`**: Generates daily, weekly, and monthly fitness reports and trends.

---

## Best Practices

- **Object-Oriented Programming**: Encapsulate user data (e.g., workouts, meals) and functionality (e.g., reminders) into classes and objects.
- **Separation of Concerns**: Each module is designed for specific functionalities (e.g., tracking workouts, meals, health stats) to ensure code reusability and maintainability.
- **User Interaction**: Clean and responsive CLI interaction with proper validation and error handling.
- **Modularity**: Code is organized into manageable, scalable modules that can be extended with new features like API integration or mobile interfaces.

---

## Extensions
This project can be extended by integrating external APIs such as:
- Fitness trackers (e.g., Fitbit, Garmin)
- Nutrition databases (e.g., MyFitnessPal)
- Mobile interfaces for on-the-go tracking.

---

## Installation and Setup

1. Clone this repository:
   ```bash
   https://github.com/HmzhDubh/UNIT-1-PROJECT.git

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt

3. Run the Tracker:
   ```bash
   python main.py

---

### Key Highlights:
- The features are clearly outlined with headings, making it easy to understand what each part of the tool does.
- The code organization section explains the modular structure of the project.
- Best practices are mentioned to emphasize the good coding standards you're following.
- Extensions provide ideas on how the project can evolve in the future.
- Installation instructions make it easy for someone to set up the project on their own machine.

This `README.md` structure follows a standard format and ensures that anyone viewing the project on GitHub or another platform will understand its purpose and how to use it.

cli_health_fitness_tracker/
│
├── workouts.py
│   ├── class Workout
│   └── functions for logging, updating, and retrieving workouts
│
├── nutrition.py
│   ├── class Meal
│   └── functions for logging, updating, and retrieving meals
│
├── health_stats.py
│   ├── class HealthStats
│   └── functions for tracking weight, BMI, and measurements
│
├── reminders.py
│   ├── class Reminder
│   └── functions for managing reminders
│
├── reports.py
│   ├── class ReportGenerator
│   └── functions for generating and displaying reports
│
├── main.py
│   └── Main program to handle user interaction
│
├── requirements.txt
│   └── List of dependencies (e.g., matplotlib)
│
└── README.md

---

### Explanation of the Structure:

- **`workouts.py`**: This module manages exercise logs, workout tracking, and goals. It includes the `Workout` class along with functions for logging, updating, and retrieving workouts.

- **`nutrition.py`**: This module handles meal logging and calorie/macronutrient tracking. It contains the `Meal` class and related functions.

- **`health_stats.py`**: Responsible for tracking user data such as weight, BMI, and body measurements. It features the `HealthStats` class with relevant functions.

- **`reminders.py`**: Manages fitness reminders for workouts, meals, and more. This module includes the `Reminder` class.

- **`reports.py`**: Generates daily, weekly, and monthly fitness reports and trends. This includes the `ReportGenerator` class.

- **`main.py`**: The entry point of the application that handles user interaction.

- **`requirements.txt`**: Lists the dependencies required for the project, such as `matplotlib`.

- **`README.md`**: This file, providing an overview and documentation for the project.

---
