# tracker/db_manager.py

import sqlite3
from .config import DB_PATH

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS market_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            symbol TEXT,
            price REAL,
            volume REAL,
            timestamp TEXT
        )
    """)
    conn.commit()
    conn.close()

def insert_data(symbol, price, volume, timestamp):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO market_data (symbol, price, volume, timestamp) VALUES (?, ?, ?, ?)",
                   (symbol, price, volume, timestamp))
    conn.commit()
    conn.close()
