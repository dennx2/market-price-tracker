from dotenv import load_dotenv
import os


# Load the .env file
load_dotenv()

# Access the variables
chat_id = os.getenv("CHAT_ID")

from tracker.forex.get_current_rate import google_exchange_rate
from tracker.forex.compose_message import compose_message
from tracker.forex.send_notification import send_notification
from tracker.model.criteria import Criteria

forex_alert: Criteria = {
    "ticker": "CADTWD=X",
    "condition": "above",
    "price_threshold": "23.5",
}

current_rate = google_exchange_rate("cadtwd")
if current_rate:
    msg = compose_message(current_rate, forex_alert)

    if msg and chat_id:
        send_notification(chat_id, msg)
