from ..model.criteria import Criteria


# forex_alert = {"ticker": "CADTWD=X", "condition": "below", "price_threshold": 23.5}


def compose_message(current_rate: float, criteria: Criteria) -> str:
    message = ""

    condition = criteria["condition"]
    price_threshold = float(criteria["price_threshold"])

    if condition == "above" and current_rate > price_threshold:
        message = f"Your alert has been triggered. The current rate is now above {criteria['price_threshold']} at {current_rate:.4f}."
    elif condition == "below" and current_rate < price_threshold:
        message = f"Your alert has been triggered. The current rate is now below {criteria['price_threshold']} at {current_rate:.4f}."

    return message
