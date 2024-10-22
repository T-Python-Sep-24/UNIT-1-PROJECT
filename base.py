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
            with tqdm(total=os.path.getsize(filePath), desc="Saving Data", ncols=100) as saving_par:

                for i in range(os.path.getsize(filePath) - 10):
                    time.sleep(0.02)
                    saving_par.update(1)

                json.dump(data, f, indent=4)
                saving_par.update(10)

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
                with tqdm(total=os.path.getsize(filePath), desc="Loading Data", ncols=100) as loading_par:
                    loading_par.colour = 'WHITE'
                    for i in range(os.path.getsize(filePath) - 10):
                        time.sleep(0.01)
                        loading_par.update(1)
                    data = json.load(file)
                    loading_par.update(10)

                return data
        except Exception as e:
            print(f"Error loading from file The File might be Empty or {e} ⚠ ")


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