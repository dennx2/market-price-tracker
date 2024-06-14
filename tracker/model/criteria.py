from typing import TypedDict, Literal


class Price_Criteria(TypedDict):
    ticker: str
    condition: Literal["above", "below"]
    price_threshold: float


class Stoch_Criteria(TypedDict):
    ticker: str
    condition: Literal["above", "below"]
    K_threshold: int
    D_threshold: int
