# Python for Finance Foundation

Python is the backbone of modern financial engineering. In this foundation, we focus on the libraries that matter most for building resilient financial systems.

## 📦 Essential Libraries
- **Pandas**: The industry standard for data manipulation and time-series analysis.
- **NumPy**: High-performance mathematical functions for array operations.
- **OpenPyXL**: Interaction with Excel files (.xlsx) for legacy system integration.
- **Matplotlib / Seaborn**: Visualizing financial trends and distributions.
- **YFinance**: For fetching market data from Yahoo Finance.

## 🛠️ Key Concepts

### 1. Vectorization
Avoid loops where possible. Pandas and NumPy are designed to operate on entire columns (vectors) at once, which is significantly faster for large financial datasets.

### 2. Time-Series Analysis
Financial data is almost always time-indexed. Mastery of `.resample()`, `.rolling()`, and `.shift()` is mandatory for calculating trends and momentum.

### 3. Precision
Use the `decimal` module for currency calculations to avoid floating-point errors common in binary representations of base-10 decimals.

## 📝 Example: Calculating Returns & Volatility
```python
import pandas as pd
import yfinance as yf

# Fetch stock data
ticker = "AAPL"
df = yf.download(ticker, start="2023-01-01", end="2023-12-31")

# Calculate daily returns
df['Returns'] = df['Adj Close'].pct_change()

# Calculate 30-day volatility (annualized)
volatility = df['Returns'].rolling(window=30).std() * (252**0.5)

print(f"Latest 30-day Annualized Volatility for {ticker}: {volatility.iloc[-1]:.2%}")
```

## 🚀 Utility Tools
See [finance_helpers.py](./finance_helpers.py) for a collection of ready-to-use utility functions for CAGR and outlier detection.

