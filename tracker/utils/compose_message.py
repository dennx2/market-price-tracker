from ..model.criteria import Price_Criteria


# forex_alert = {"ticker": "CADTWD=X", "condition": "below", "price_threshold": 23.5}


def compose_price_alert(current_rate: float, criteria: Price_Criteria) -> str:
    message = ""

    ticker = criteria["ticker"]
    condition = criteria["condition"]
    price_threshold = criteria["price_threshold"]

    if condition == "above" and current_rate > price_threshold:
        message = f"Your alert for {ticker} has been triggered. The current rate is now above {criteria['price_threshold']} at {current_rate:.4f}."
    elif condition == "below" and current_rate < price_threshold:
        message = f"Your alert for {ticker} has been triggered. The current rate is now below {criteria['price_threshold']} at {current_rate:.4f}."

    return message
