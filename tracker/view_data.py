# tracker/view_data.py
import sqlite3

conn = sqlite3.connect("data/market_data.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM market_data ORDER BY timestamp DESC LIMIT 5;")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()
