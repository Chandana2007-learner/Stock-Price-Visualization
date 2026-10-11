# Stock Price Visualization

## Goal
Analyze historical closing prices, plot the closing price, and add 20-day and 50-day moving averages.

## Tools
- Python
- Pandas
- Matplotlib
- yfinance (downloads historical market data)

## Setup
Open this folder in VS Code, then open Terminal and run:

```bash
python -m pip install pandas matplotlib yfinance
python stock_visualization.py
```

The script downloads one year of Microsoft (MSFT) prices by default and saves CSV data in `data/` and a chart in `charts/`.

If downloading data does not work, open `stock_visualization.py`, change `USE_SAMPLE_DATA = False` to `USE_SAMPLE_DATA = True`, and run it again. The included sample dataset is illustrative, not actual market data.

## Change the stock
Edit `TICKER` in `stock_visualization.py`. Examples:
- `AAPL` — Apple
- `GOOGL` — Alphabet
- `RELIANCE.NS` — Reliance Industries on NSE
- `TCS.NS` — TCS on NSE

For Indian stocks, change the y-axis label to `Closing Price (INR)` if you want the chart label to reflect rupees.

## Moving averages
- 20-day moving average: average of the latest 20 trading-day closing prices.
- 50-day moving average: average of the latest 50 trading-day closing prices.

## Short interpretation template
1. The closing-price line shows how the stock price changed during the period.
2. The 20-day moving average responds more quickly to recent price changes than the 50-day average.
3. Compare the two averages to describe short-term versus longer-term momentum. Moving averages alone do not predict future prices or provide investment advice.

## Project deliverables
- `stock_visualization.py` — analysis code
- `data/sample_stock_prices.csv` — sample data for offline testing
- `data/stock_prices_with_moving_averages.csv` — generated after running
- `charts/stock_price_moving_averages.png` — generated after running
- Stock Price Graph
