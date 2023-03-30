import requests
import os
from dotenv import load_dotenv
from flight_data import FlightData


load_dotenv("D:/Python_learning/Python_course/venv/environment_variables.env")
KIWI_API_KEY = os.getenv("KIWI_TEQUILA_API_KEY")
KIWI_ENDPOINT = "https://api.tequila.kiwi.com"



headers = {"apikey": KIWI_API_KEY}
query = {
    "fly_from": "LGA",
    "date_from": "01/04/2023",
    "date_to": "05/05/2023",
}

response = requests.get(url=f"{KIWI_ENDPOINT}/v2/search", headers=headers, params=query)

try:
    data = response.json()
    print(data)
except IndexError:
    print(f"No flights found for .")

