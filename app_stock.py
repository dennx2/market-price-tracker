from tracker.stock.get_data import *
from tracker.stock.technical_analysis import *

df = get_data("00934.TW", period="1mo")
# prerequisite: get historical quotes from your own source
quotes = transform_data_to_quotes(df)
# example: get 20-period simple moving average
result = run_sma(quotes, 5, candle_part=CandlePart.CLOSE)
# use results as needed for your use case (example only)

print(f"SMA on {result.date.date()} was ${result.sma or 0:.4f}")
