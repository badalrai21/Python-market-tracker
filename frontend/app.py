from flask import Flask, render_template
import sqlite3
import os

app = Flask(__name__)

def get_market_data():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DB_PATH = os.path.join(BASE_DIR, '..', 'data', 'market_data.db')
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM market_data ORDER BY timestamp DESC LIMIT 10")
    rows = cursor.fetchall()
    conn.close()
    return rows

@app.route('/')
def dashboard():
    data = get_market_data()
    return render_template('dashboard.html', data=data)

if __name__ == '__main__':
    # For local testing
    app.run(debug=True, host='0.0.0.0', port=10000)
