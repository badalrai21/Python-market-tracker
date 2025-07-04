# tracker/config.py

SYMBOL = "BTCUSDT"
API_URL = f"https://api.binance.com/api/v3/ticker/24hr?symbol={SYMBOL}"
DB_PATH = "data/market_data.db"
LOG_PATH = "logs/daily_log.txt"
THRESHOLD_PERCENT = 5
