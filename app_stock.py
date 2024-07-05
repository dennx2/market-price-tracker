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

stoch_00929: Stoch_Criteria = {
    "ticker": "00929.TW",
    "speed": "fast",
    "overbought_threshold": 80,
    "oversold_threshold": 20,
}

stoch_00934: Stoch_Criteria = {
    "ticker": "00934.TW",
    "speed": "fast",
    "overbought_threshold": 80,
    "oversold_threshold": 20,
}

stoch_00936: Stoch_Criteria = {
    "ticker": "00936.TW",
    "speed": "fast",
    "overbought_threshold": 80,
    "oversold_threshold": 20,
}

stoch_00940: Stoch_Criteria = {
    "ticker": "00940.TW",
    "speed": "fast",
    "overbought_threshold": 80,
    "oversold_threshold": 20,
}

criterias: list[Stoch_Criteria] = [stoch_00929, stoch_00934, stoch_00936, stoch_00940]


def main():

    for critera in criterias:
        df = get_data(critera["ticker"], period="3mo")
        quotes = transform_data_to_quotes(df)

        stoch_result = run_stoch(quotes, smoothK=critera["speed"])
        if stoch_result:
            msg = compose_stoch_alert(stoch_result, critera)

            if msg and chat_id:
                send_to_telegram(chat_id, msg)


main()
