import requests
import os
from dotenv import load_dotenv
from pprint import pprint

load_dotenv("D:/Python_learning/Python_course/venv/environment_variables.env")
bearer_token = os.getenv("SHEETY_BEARER_TOKEN")
SHEETY_ENDPOINT = "https://api.sheety.co/92ee1353de977ac5b50ce7c9c318ec0d/flightDeals/prices"

headers = {
        "Authorization": bearer_token,
    }


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_ENDPOINT, headers=headers)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_code(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_ENDPOINT}/{city['id']}",
                json=new_data,
                headers=headers,
            )
            print(response.text)
