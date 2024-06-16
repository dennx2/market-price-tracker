from stock_indicators import indicators
from stock_indicators.indicators.common.quote import Quote
from stock_indicators.indicators.common.enums import CandlePart
from stock_indicators.indicators.common.enums import MAType
from stock_indicators.indicators.sma import SMAResult
from stock_indicators.indicators.stoch import StochResult

from ..utils.logger import setup_logger

logger = setup_logger()


def run_stoch(quotes: list[Quote], speed="slow") -> StochResult:

    if speed == "slow":
        smooth_periods = 3
    else:
        smooth_periods = 1

    results = indicators.get_stoch(
        quotes,
        lookback_periods=14,
        signal_periods=3,
        smooth_periods=smooth_periods,
        ma_type=MAType.SMA,
    )

    result = results[-1]
    if result.k and result.d:
        logger.info(f"K:{result.k:.2f} | D:{result.d:.2f}")
    else:
        logger.error(f"Failed to calculate Stochastic KD.")
    return result


def run_sma(
    quotes: list[Quote], periods: int, candle_part: CandlePart = CandlePart.CLOSE
) -> SMAResult:

    # if periods >= len(quotes):
    #     logger.error(
    #         f"The number of periods ({periods}) must be less than the number of quotes ({len(quotes)})."
    #     )
    #     raise ValueError(f"Something wrong with sma calculation.")

    results = indicators.get_sma(
        quotes, lookback_periods=periods, candle_part=candle_part
    )

    result = results[-1]
    if result.sma:
        logger.info(f"SMA was ${result.sma:.2f}")
    else:
        logger.error(f"Failed to calculate SMA.")
    return result
