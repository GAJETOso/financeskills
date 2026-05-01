# Financial APIs

Accessing high-quality, real-time, and historical financial data is critical for any finance skill.

## 🌐 Top Financial APIs
1.  **Alpha Vantage**: Wide range of stock, crypto, and forex data. Great for technical indicators.
2.  **Polygon.io**: High-performance market data with low latency.
3.  **IEX Cloud**: Institutional-grade data for retail developers.
4.  **Yahoo Finance (via yfinance)**: Free, community-maintained access to global markets.
5.  **SEC EDGAR**: The source of truth for US public company filings (10-K, 10-Q).

## 🛡️ Best Practices
- **Rate Limiting**: Always implement exponential backoff when hitting free-tier APIs.
- **Key Management**: Never hardcode API keys. Use `.env` files and `os.getenv()`.
- **Data Caching**: Store expensive API responses locally in Parquet or CSV format to avoid redundant calls.
- **Normalization**: Different APIs use different column naming conventions. Always normalize data to a standard schema (e.g., `date`, `open`, `high`, `low`, `close`, `volume`).

## 📝 Example: API Request with Backoff
```python
import time
import requests

def fetch_with_retry(url, retries=3):
    for i in range(retries):
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 429: # Rate limit
            time.sleep(2 ** i)
    return None
```
