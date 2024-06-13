import yfinance as yf
from ..utils.logger import setup_logger
from tracker.model.criteria import Price_Criteria

logger = setup_logger()


def get_price(ticker: str):
    t = yf.Ticker(ticker)


def trigger_alert(criteria: Price_Criteria) -> str:
    message = ""
    # is_triggered = check_criteria()
    # if is_triggered:
    #   create message

    return message
