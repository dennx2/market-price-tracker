from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv()

# Access the variables
chat_id = os.getenv("CHAT_ID")


from tracker.stock.get_data import *
from tracker.stock.technical_analysis import *
from tracker.utils.compose_message import *
from tracker.utils.send_notification import send_to_telegram

# df = get_data("00934.TW", period="1mo")
# quotes = transform_data_to_quotes(df)

# sma_result = run_sma(quotes, 60)

stoch_alert_criteria: Stoch_Criteria = {
    "ticker": "00929.TW",
    "speed": "fast",
    "overbought_threshold": 80,
    "oversold_threshold": 20,
}


def main():
    df = get_data(stoch_alert_criteria["ticker"], period="3mo")
    quotes = transform_data_to_quotes(df)

    stoch_result = run_stoch(quotes, stoch_alert_criteria["speed"])
    if stoch_result:
        msg = compose_stoch_alert(stoch_result, stoch_alert_criteria)

        if msg and chat_id:
            send_to_telegram(chat_id, msg)


main()
