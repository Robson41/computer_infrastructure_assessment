#!/usr/bin/env python3
"""
FAANG Data Script

This script:
1. Downloads hourly stock data for the past 5 days for FAANG stocks.
2. Saves each stock CSV in the 'data' folder with a timestamp.
3. Plots the Close prices for all FAANG stocks on a single plot.
4. Saves the plot in the 'plots' folder with a timestamp.
"""

import os
from datetime import datetime
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# ------------------------------
# Function: get_data
# ------------------------------
def get_data():
    """Download FAANG stock data and save CSVs in 'data' folder."""
    faang_stocks = ["META", "AAPL", "AMZN", "NFLX", "GOOG"]
    data_folder = "data"
    os.makedirs(data_folder, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    
    for ticker in faang_stocks:
        df = yf.download(ticker, period="5d", interval="1h")
        if not df.empty:
            filename = f"{ticker}_{timestamp}.csv"
            file_path = os.path.join(data_folder, filename)
            df.to_csv(file_path)
            print(f"Saved {ticker} data to {file_path}")
        else:
            print(f"No data downloaded for {ticker}")

# ------------------------------
# Function: plot_data
# ------------------------------
def plot_data():
    """Load latest FAANG CSVs and plot Close prices."""
    data_folder = "data"
    plots_folder = "plots"
    os.makedirs(plots_folder, exist_ok=True)

    # Load latest CSVs
    faang_data = {}
    csv_files = sorted([f for f in os.listdir(data_folder) if f.endswith(".csv")])
    latest_files = {}
    for ticker in ["META", "AAPL", "AMZN", "NFLX", "GOOG"]:
        # Get latest file for each ticker
        ticker_files = [f for f in csv_files if f.startswith(ticker)]
        if ticker_files:
            latest_files[ticker] = ticker_files[-1]
            df = pd.read_csv(os.path.join(data_folder, latest_files[ticker]), index_col=0)
            df.index = pd.to_datetime(df.index, errors="coerce")
            df[["Open", "High", "Low", "Close", "Adj Close", "Volume"]] = \
                df[["Open", "High", "Low", "Close", "Adj Close", "Volume"]].astype(float)
            faang_data[ticker] = df

    # Plot Close prices
    plt.figure(figsize=(14,7))
    for ticker, df in faang_data.items():
        plt.plot(df.index, df['Close'], label=ticker)

    latest_date = max(df.index.max() for df in faang_data.values()).strftime("%Y-%m-%d")
    plt.title(f"FAANG Stocks Close Prices as of {latest_date}")
    plt.xlabel("Datetime")
    plt.ylabel("Close Price (USD)")
    plt.legend()
    plt.grid(True)

    # Save plot
    os.makedirs(plots_folder, exist_ok=True)
    filename = datetime.now().strftime("%Y%m%d-%H%M%S.png")
    file_path = os.path.join(plots_folder, filename)
    plt.savefig(file_path)
    plt.show()
    print(f"Plot saved to {file_path}")

# ------------------------------
# Main execution
# ------------------------------
if __name__ == "__main__":
    get_data()
    plot_data()

