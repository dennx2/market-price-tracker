from tracker.stock.get_data import *
from tracker.stock.technical_analysis import *

df = get_data("00934.TW", period="1mo")
quotes = transform_data_to_quotes(df)

sma_result = run_sma(quotes, 5)
print(f"SMA on {sma_result.date.date()} was ${sma_result.sma or 0:.4f}")

stoch_result = run_stoch(quotes, speed="fast")
print(f"{stoch_result.date.date()} | K:{stoch_result.k:.2f} | D:{stoch_result.d:.2f}")
