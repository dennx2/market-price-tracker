from stock_indicators.indicators.stoch import StochResult

from ..model.criteria import *


def compose_price_alert(current_quote: float, criteria: Price_Criteria) -> str:
    message = ""

    ticker = criteria["ticker"]
    condition = criteria["condition"]
    price_threshold = criteria["price_threshold"]

    if condition == "above" and current_quote > price_threshold:
        message = f"Your alert for {ticker} has been triggered. The current rate is now above {price_threshold} at {current_quote:.4f}."
    elif condition == "below" and current_quote < price_threshold:
        message = f"Your alert for {ticker} has been triggered. The current rate is now below {price_threshold} at {current_quote:.4f}."

    return message


def compose_stoch_alert(current_stoch: StochResult, criteria: Stoch_Criteria) -> str:
    message = ""

    ticker = criteria["ticker"]
    overbought_threshold = criteria["overbought_threshold"]
    oversold_threshold = criteria["oversold_threshold"]

    if current_stoch.k < oversold_threshold and current_stoch.d < oversold_threshold:
        message = f"Stock ticker {ticker} is oversold. K:{current_stoch.k:.2f} | D:{current_stoch.d:.2f}"
    # elif (
    #     current_stoch.k > overbought_threshold
    #     and current_stoch.d > overbought_threshold
    # ):
    #     message = f"Stock ticker {ticker} is overbought. K:{current_stoch.k:.2f} | D:{current_stoch.d:.2f}"

    return message
