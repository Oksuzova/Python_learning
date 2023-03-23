import requests
import os
from dotenv import load_dotenv

load_dotenv("D:/Python_learning/Python_course/venv/environment_variables.env")


def telegram_bot_sendtext(bot_message):
    bot_token = os.getenv("BOT_TOKEN")
    bot_chatID = os.getenv("BOT_CHATID")
    send_text = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={bot_chatID}&parse_mode=Markdown&text={bot_message}"
    response = requests.get(send_text)
    return response.json()


api_key = "72aa68d607efa9ce6ec281ee626fc20d"

parameters = {
    "lat": 50.355630,
    "lon": 30.989099,
    "units": "metric",
    "appid": api_key,
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()

data = response.json()
will_rain = False

for time in range(0, 20):
    if data["list"][time]["weather"][0]["id"] < 700:
        will_rain = True

if will_rain:
    telegram_bot_sendtext("Bring the umbrella! ☔️")


















