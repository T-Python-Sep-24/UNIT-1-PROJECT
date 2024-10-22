import json
import os
def save_results(user_results):
    # Save user results to a JSON file.
    with open('results.json', 'a') as f:
        json.dump(user_results, f)
        f.write('\n')  

def load_results():
    if os.path.exists('results.json'):
        with open('results.json', 'r') as f:
            return [json.loads(line) for line in f]
    else:
        return []  # Return an empty list if the file does not exist

    