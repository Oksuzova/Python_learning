import requests
import os
from dotenv import load_dotenv
import datetime as dt

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
QUANT_ARTICLES = 1


# ----------------------------------GROWTH PERCENTAGE--------------------------------------------------------#

load_dotenv("D:/Python_learning/Python_course/venv/environment_variables.env")
alpha_api_key = os.getenv("ALPHA_API_KEY")

now = dt.datetime.now()
yesterday = str(now.date() - dt.timedelta(days=1))
day_bef_yesterday = str(now.date() - dt.timedelta(days=2))


parameters = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "outputsize": "compact",
    "apikey": alpha_api_key,
}

response = requests.get(url="https://www.alphavantage.co/query", params=parameters)
data = response.json()

yesterday_data = float(data["Time Series (Daily)"][yesterday]["4. close"])
day_bef_yesterday_data = float(data["Time Series (Daily)"][day_bef_yesterday]["4. close"])

difference = abs(float(yesterday_data - day_bef_yesterday_data))
percent = round(difference * 100 / yesterday_data)

if yesterday_data > day_bef_yesterday_data:
    index = "🔺"
else:
    index = "🔻"

# ----------------------------------------------NEWS--------------------------------------------------------#

load_dotenv("D:/Python_learning/Python_course/venv/environment_variables.env")
news_api_key = os.getenv("NEWS_API_KEY")

parameters = {
    "q": COMPANY_NAME,
    "searchIn": "title",
    "sortBy": "popularity",
    "apiKey": news_api_key,
}

news_response = requests.get(url="https://newsapi.org/v2/everything", params=parameters)
articles = news_response.json()["articles"]

three_articles = articles[:QUANT_ARTICLES]

data_articles = [f"{STOCK}: {index}{percent} \nHeadline: {articles['title']}. \nBrief: {articles['description']}" for articles in three_articles]


# ----------------------------------------------SENDING MESSAGE--------------------------------------------------------#

def telegram_bot_sendtext(bot_message):
    bot_token = os.getenv("BOT_TOKEN")
    bot_chatID = os.getenv("BOT_CHATID")
    send_text = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={bot_chatID}&parse_mode=Markdown&text={bot_message}"
    response_tg = requests.get(send_text)
    return response_tg.json()


for article in data_articles:
    if percent > 5:
        telegram_bot_sendtext(article)
