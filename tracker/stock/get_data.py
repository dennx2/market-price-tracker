import yfinance as yf
from pandas import DataFrame
from stock_indicators.indicators.common.quote import Quote

from ..utils.logger import setup_logger
from tracker.model.criteria import Price_Criteria

logger = setup_logger()


def get_data(ticker: str, period: str = "3yr") -> DataFrame:
    df = (
        yf.Ticker(ticker).history(period=period)
        # .sort_values(by="Date", ascending=False)
        .reset_index()
    )

    return df


def transform_data_to_quotes(df: DataFrame) -> list[Quote]:
    quotes = [
        Quote(d, o, h, l, c, v)
        for d, o, h, l, c, v in zip(
            df["Date"],
            df["Open"],
            df["High"],
            df["Low"],
            df["Close"],
            df["Volume"],
        )
    ]
    return quotes
