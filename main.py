import requests
from datetime import datetime

APP_ID = "nutritionix id"
API_KEY = "nutritionix iapi key"
GENDER = "whatever"
HEIGHT_CM = "in cm"
AGE = 0 # Your age in integer

now = datetime.now()
date = now.strftime("%m/%d/%Y")
time = now.strftime("%H:%M:%S")

query = input("What exercise did you do today?")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0",
}

parameters = {
    "query": query,
    "gender": GENDER,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

exercise_endpoint ="trackapi url"

response = requests.post(url=exercise_endpoint,json=parameters, headers=headers)
result = response.json()["exercises"]

for activity in result:
    exercise = activity["name"].title()
    duration = activity["duration_min"]
    calories = activity["nf_calories"]

    headers_2 = {
        "Authorization": "Bearer (your sheety key goes here)",
    }
    parameters_2 = {

        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise,
            "duration": duration,
            "calories": calories,
            }
    }

    sheety_endpoint = "sheety url"

    response_2 = requests.post(url=sheety_endpoint, json=parameters_2, headers=headers_2)

print(response_2.text)