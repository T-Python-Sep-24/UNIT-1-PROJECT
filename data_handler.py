import json

def load_data_from_json(file_path:str):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {"teachers": [], "students": [], "courses": []}

def save_data_to_json(file_path:str, data:dict):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)
