import time
from tqdm import tqdm

# Function to simulate waiting for an API response
def wait_for_response():
    print("Waiting for API response:")
    for _ in tqdm(range(100), desc="Processing", ascii=True, ncols=100):
        time.sleep(0.05)

# Call the waiting function
wait_for_response()

# Proceed with your API call
print("API response received!")
