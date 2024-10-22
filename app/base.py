import json
import os.path
import time

from tqdm import tqdm

def save_to_file(filePath: str, data):
    """
    This method save the accounts data to the pickle file after it has been serialized
    :param fileName:
    :return:
    """
    try:
        with open(filePath, 'w') as f:

            json.dump(data, f, indent=4)

    except Exception as e:
        print(e)


def load_from_file(filePath):
    """
    This method loads all the accounts data from the pickle file and deserialize it
    :param fileName:
    :return: accounts
    """
    if os.path.getsize(filePath) > 0:
        try:
            with open(filePath, 'r') as file:
                # print(f"Loading Data ... ⏳")
                data = json.load(file)
                return data
        except Exception as e:
            print(f"Error loading from file The File might be Empty or {e} ⚠ ")
            # return []
    else:
        print(f"File {filePath} is Empty")
        if not filePath == '../user_data_files/user.json':
            return []

def clear_files(f1,f2,f3):
    """
    This method clear all data from the files
    :param filePath:
    :return:
    """
    filePaths = [f1, f2, f3]
    try:
        for file in filePaths:
            with open(file, 'w') as f:
                json.dump([], f)
        print("Data Cleared Successfully")
    except Exception as e:
        print(e)
