from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv()

# Access the variables
chat_id = os.getenv("CHAT_ID")

from tracker.model.criteria import Price_Criteria
from tracker.forex.get_data import google_exchange_rate
from tracker.utils.compose_message import *
from tracker.utils.send_notification import send_to_telegram

forex_alert_criteria: Price_Criteria = {
    "ticker": "CADTWD",
    "condition": "below",
    "price_threshold": 23.5,
}


def main():
    current_rate = google_exchange_rate(forex_alert_criteria["ticker"])
    if current_rate:
        msg = compose_price_alert(current_rate, forex_alert_criteria)

        if msg and chat_id:
            send_to_telegram(chat_id, msg)


main()
