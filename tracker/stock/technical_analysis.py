from datetime import date
from stock_indicators import indicators
from stock_indicators.indicators.common.quote import Quote
from stock_indicators.indicators.common.enums import CandlePart
from stock_indicators.indicators.sma import SMAResult

from ..utils.logger import setup_logger

logger = setup_logger()


def run_stoch(quotes: Quote):
    pass


def run_sma(quotes: list[Quote], periods: int, candle_part: CandlePart) -> SMAResult:

    if periods >= len(quotes):
        logger.error(
            f"The number of periods ({periods}) must be less than the number of quotes ({len(quotes)})."
        )
        raise ValueError(f"Something wrong with sma calculation.")

    results = indicators.get_sma(quotes, periods, candle_part=candle_part)
    if not results:
        logger.error(f"No sma result")
        raise ValueError(f"Something wrong with sma calculation.")

    return results[-1]
