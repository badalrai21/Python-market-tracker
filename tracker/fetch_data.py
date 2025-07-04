# tracker/fetch_data.py

import requests
import datetime
from .config import API_URL, SYMBOL

def fetch_market_data():
    try:
        response = requests.get(API_URL)
        data = response.json()
        price = float(data["lastPrice"])
        volume = float(data["volume"])
        timestamp = datetime.datetime.now().isoformat()
        return SYMBOL, price, volume, timestamp
    except Exception as e:
        print("[ERROR] Fetch failed:", e)
        return None
