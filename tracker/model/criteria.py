from typing import TypedDict, Literal


class Criteria(TypedDict):
    ticker: str
    condition: Literal["above", "below"]
    price_threshold: float
