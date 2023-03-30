import requests
import os
from dotenv import load_dotenv
from flight_data import FlightData


load_dotenv("D:/Python_learning/Python_course/venv/environment_variables.env")
KIWI_API_KEY = os.getenv("KIWI_TEQUILA_API_KEY")
KIWI_ENDPOINT = "https://api.tequila.kiwi.com"


class FlightSearch:

    def get_destination_code(self, city_name):
        headers = {
            "apikey": KIWI_API_KEY,
        }

        parameters = {
            "term": city_name,
        }

        response = requests.get(url=KIWI_ENDPOINT, params=parameters, headers=headers)
        data = response.json()
        code = data["locations"][0]["code"]
        return code

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        headers = {"apikey": KIWI_API_KEY}
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }

        response = requests.get(
            url=f"{KIWI_ENDPOINT}/v2/search",
            headers=headers,
            params=query,
        )

        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination_city_code}.")
            return None

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        print(f"{flight_data.destination_city}: £{flight_data.price}")
        return flight_data
