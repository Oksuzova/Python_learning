import requests
import os
from dotenv import load_dotenv
import datetime as dt


query = input("Tell me which exercise you did: ")

load_dotenv("D:/Python_learning/Python_course/venv/environment_variables.env")

app_id = os.getenv("NUTRIT_APP_ID")
apy_key = os.getenv("NUTRIT_API_KEY")
bearer_token = os.getenv("SHEETY_BEARER_TOKEN")

nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": app_id,
    "x-app-key": apy_key,
}

user_parameters = {
    "query": query,
}

response = requests.post(url=nutritionix_endpoint, json=user_parameters, headers=headers)
data = response.json()

sheety_endpoint = "https://api.sheety.co/92ee1353de977ac5b50ce7c9c318ec0d/workoutTracking/workouts"


data_exercise = data["exercises"]


for exercise in data_exercise:

    headers = {
        "Authorization": bearer_token,
    }

    date = dt.datetime.now().strftime("%d/%m/%Y")
    time = dt.datetime.now().strftime("%H:%M:%S")
    action = exercise["name"]
    duration = exercise["duration_min"]
    calories = exercise["nf_calories"]

    row_data = {
        "workout":
            {
                "date": date,
                "time": time,
                "exercise": action.title(),
                "duration": duration,
                "calories": calories,
                "id": 2
            }
    }

    sheety_response = requests.post(url=sheety_endpoint, json=row_data, headers=headers)














