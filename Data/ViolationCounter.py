import pickle
import os

COUNTER_FILE = "violation_counter.pkl"

def load_violation_counter():
    if os.path.exists(COUNTER_FILE):
        with open(COUNTER_FILE, "rb") as file:
            return pickle.load(file)
    return 1  # Start from 1 if the file doesn't exist

def save_violation_counter(counter):
    with open(COUNTER_FILE, "wb") as file:
        pickle.dump(counter, file)
