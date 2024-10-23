import json

def save_results(user_results):
    #Save user results to a JSON file.
    with open('results.json', 'a') as f:
        json.dump(user_results, f)
        f.write('\n ')  # Newline for separating entries

def load_results():
    #Load user results from a JSON file.
    try:
        with open('results.json', 'r') as f:
            return [json.loads(line) for line in f]
    except FileNotFoundError:
        return []  # Return an empty list if file does not exist