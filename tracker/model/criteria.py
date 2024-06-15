from typing import TypedDict, Literal


class Price_Criteria(TypedDict):
    ticker: str
    condition: Literal["above", "below"]
    price_threshold: float


class Stoch_Criteria(TypedDict):
    ticker: str
    speed: Literal["slow", "fast"]
    overbought_threshold: int
    oversold_threshold: int
