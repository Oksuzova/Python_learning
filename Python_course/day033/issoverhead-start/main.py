import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 50.355630
MY_LONG = 30.989099

time_now = datetime.now()
TODAY = time_now.date()

my_email = "testanya289@gmail.com"
password = "mjiphmycpctqztmv"


def check_position():
    global MY_LAT, MY_LONG
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    my_position = (MY_LAT, MY_LONG)
    iss_position_plus = (iss_latitude + 5, iss_longitude + 5)
    iss_position_min = (iss_latitude - 5, iss_longitude - 5)

    if iss_position_min <= my_position >= iss_position_plus:
        return True
    else:
        return False


# position is within +5 or -5 degrees of the ISS position.

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "date": TODAY,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0]) + 2
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0]) + 2

while True:
    time.sleep(60)
    if check_position():
        if sunrise > int(time_now.hour) > sunset:
            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs="42toks@gmail.com",
                    msg=f"Subject: Look up!\n\nISS is up in the sky now!"
                )
