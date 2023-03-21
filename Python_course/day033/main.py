# import requests
#
# response = requests.get("http://api.open-notify.org/iss-now.json")
# # print(response.status_code)
# response.raise_for_status()
#
# data = response.json()
# print(data)
#
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
#
# iss_position = (longitude, latitude)
#
# print(iss_position)


import requests
import datetime as dt


MY_LAT = 50.355630
MY_LNG = 30.989099
now = dt.datetime.now()
TODAY = now.date()

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "date": TODAY,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

data = response.json()
sunrise = "0" + str(int(data["results"]["sunrise"].split("T")[1].split(":")[0]) + 2)
sunset = str(int(data["results"]["sunset"].split("T")[1].split(":")[0]) + 2)

print(sunrise)
print(int(now.hour))
print(sunset)

