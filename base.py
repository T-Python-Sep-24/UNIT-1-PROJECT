import json

def save_to_file(fileName):
    """
    This method save the accounts data to the pickle file after it has been serialized
    :param fileName:
    :return:
    """
    try:
        with open(fileName, 'w') as f:
            json.dump(workouts, f, indent=4)
    except Exception as e:
        print(e)

def load_from_file(fileName):
    """
    This method loads all the accounts data from the pickle file and deserialize it
    :param fileName:
    :return: accounts
    """

    try:
        with open(fileName, 'r') as file:
            workouts = json.load(file)
            print(f"Loading Data ... ⏳")
            return workouts
    except Exception as e:
        print(f"Error loading from file The File might be Empty or {e} ⚠ ")