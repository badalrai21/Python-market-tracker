# tracker/main.py

import schedule
import time
from .db_manager import init_db, insert_data
from .fetch_data import fetch_market_data
from .analyzer import detect_anomalies
from .logger import log_message

def run_tracker():
    result = fetch_market_data()
    if result:
        symbol, price, volume, timestamp = result
        insert_data(symbol, price, volume, timestamp)
        log_message(f"[DATA] {timestamp} | {symbol} | Price: {price} | Volume: {volume}")

        alert = detect_anomalies()
        if alert:
            log_message(alert)

def main():
    init_db()
    run_tracker()  # Run once at start
    schedule.every(5).minutes.do(run_tracker)

    print("[TRACKER STARTED] Running every 5 minutes.")
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
