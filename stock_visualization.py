"""
Stock Price Visualization Project
Beginner-friendly project using Python, Pandas, and Matplotlib.

Install dependencies:
    python -m pip install pandas matplotlib yfinance

Run:
    python stock_visualization.py

By default, the script downloads one year of historical data for Microsoft (MSFT).
You can change TICKER below, or set USE_SAMPLE_DATA = True to run with the included
sample CSV when internet access is unavailable.
"""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

PROJECT_DIR = Path(__file__).resolve().parent
DATA_DIR = PROJECT_DIR / "data"
CHARTS_DIR = PROJECT_DIR / "charts"
DATA_DIR.mkdir(exist_ok=True)
CHARTS_DIR.mkdir(exist_ok=True)

TICKER = "MSFT"  # Example: AAPL, GOOGL, RELIANCE.NS, TCS.NS
PERIOD = "1y"
USE_SAMPLE_DATA = False  # Change to True if download fails or internet is unavailable


def load_stock_data():
    if USE_SAMPLE_DATA:
        file_path = DATA_DIR / "sample_stock_prices.csv"
        df = pd.read_csv(file_path, parse_dates=["Date"])
        return df

    try:
        import yfinance as yf
        df = yf.download(TICKER, period=PERIOD, auto_adjust=False, progress=False)
        if df.empty:
            raise ValueError("No stock data returned. Check the ticker or internet connection.")
        # yfinance may return MultiIndex columns in newer versions.
        if isinstance(df.columns, pd.MultiIndex):
            df.columns = df.columns.get_level_values(0)
        df = df.reset_index()
        df = df[["Date", "Close"]].dropna()
        df.to_csv(DATA_DIR / f"{TICKER.replace('.', '_')}_stock_prices.csv", index=False)
        return df
    except Exception as exc:
        print(f"Could not download live data: {exc}")
        print("Using included sample data instead.")
        return pd.read_csv(DATA_DIR / "sample_stock_prices.csv", parse_dates=["Date"])


def main():
    df = load_stock_data()
    df["Date"] = pd.to_datetime(df["Date"])
    df = df.sort_values("Date").dropna(subset=["Close"])
    df["MA20"] = df["Close"].rolling(window=20).mean()
    df["MA50"] = df["Close"].rolling(window=50).mean()

    # Save the cleaned data and moving-average columns.
    df.to_csv(DATA_DIR / "stock_prices_with_moving_averages.csv", index=False)

    plt.figure(figsize=(12, 6))
    plt.plot(df["Date"], df["Close"], label="Closing Price", linewidth=1.5)
    plt.plot(df["Date"], df["MA20"], label="20-Day Moving Average", linewidth=1.5)
    plt.plot(df["Date"], df["MA50"], label="50-Day Moving Average", linewidth=1.5)
    plt.title(f"{TICKER} Stock Price Visualization")
    plt.xlabel("Date")
    plt.ylabel("Closing Price (USD for MSFT)")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    chart_path = CHARTS_DIR / "stock_price_moving_averages.png"
    plt.savefig(chart_path, dpi=150)
    plt.show()

    print("\n--- Quick Summary ---")
    print(f"Rows analyzed: {len(df)}")
    print(f"First closing price: {df['Close'].iloc[0]:.2f}")
    print(f"Latest closing price: {df['Close'].iloc[-1]:.2f}")
    change = (df["Close"].iloc[-1] / df["Close"].iloc[0] - 1) * 100
    print(f"Price change over available period: {change:.2f}%")
    print(f"Chart saved to: {chart_path}")
    print("\n--- Interpretation guide ---")
    print("1. If the closing price is mostly rising, the stock had an overall upward trend.")
    print("2. The 20-day average reacts faster to recent changes than the 50-day average.")
    print("3. When the 20-day average is above the 50-day average, recent prices have been")
    print("   stronger than the longer-term average; this alone is not a buy/sell signal.")


if __name__ == "__main__":
    main()
