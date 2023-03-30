import requests
import os
from dotenv import load_dotenv

load_dotenv("D:/Python_learning/Python_course/venv/environment_variables.env")


class NotificationManager:

    def telegram_bot_sendtext(self, bot_message):
        bot_token = os.getenv("BOT_TOKEN")
        bot_chatid = os.getenv("BOT_CHATID")
        send_text = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={bot_chatid}&parse_mode=Markdown&text={bot_message}"
        response_tg = requests.get(send_text)
        return response_tg.json()
