from generators import DataGenerators
from data_manager import DataManager

def main():
    print("Welcome to the Sales and Marketing Management System!")
    data_generator = DataGenerators()
    data_manager = DataManager()

    while True:
        command = input("> ").strip().lower()
