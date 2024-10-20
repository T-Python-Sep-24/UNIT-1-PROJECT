import requests

url = "https://calories-burned-by-api-ninjas.p.rapidapi.com/v1/caloriesburned"

querystring = {"activity":"skiing"}

headers = {
    "x-rapidapi-key": "9322ab61b2msh71fad9a1b659dc6p188339jsn524d15ec2402",
    "x-rapidapi-host": "calories-burned-by-api-ninjas.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())




