# tracker/analyzer.py

import pandas as pd
import sqlite3
from .config import DB_PATH, THRESHOLD_PERCENT

def detect_anomalies():
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query("SELECT * FROM market_data ORDER BY timestamp DESC LIMIT 5", conn)
    conn.close()

    if len(df) < 2:
        return None

    current = df.iloc[0]['price']
    previous = df.iloc[1]['price']
    change = abs((current - previous) / previous * 100)

    if change > THRESHOLD_PERCENT:
        return f"[ALERT] Price moved {change:.2f}%: {previous} → {current}"
    return None
