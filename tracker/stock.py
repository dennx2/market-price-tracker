import yfinance as yf
from utils.logger import setup_logger
from tracker.model.criteria import Criteria

logger = setup_logger()

def get_price(ticker: str):
    t = yf.Ticker(ticker)


def trigger_alert(criteria: Criteria) -> str:
    message = ""
    # is_triggered = check_criteria()
    # if is_triggered:
    #   create message

    return message


def run():
    forex_alert = {"ticker": "CADTWD=X", "condition": "below", "price_threshold": 23.5}
    get_price(forex_alert["ticker"])


if __name__ == "__main__":
    print("Hello there")
