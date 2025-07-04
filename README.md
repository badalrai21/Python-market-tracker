# 🌐 Python Market Tracker – Real-Time Crypto Dashboard

![License](https://img.shields.io/badge/license-MIT-green)
![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-3.1.1-yellow?logo=flask)

This project tracks real-time cryptocurrency market data (e.g., BTCUSDT) using Binance API and stores it in a local SQLite database. It includes a simple Flask-based frontend dashboard to display the most recent market data.

---

## 📁 Project Structure

Python-market-tracker/
├── tracker/  
│ ├── main.py ← Main script (runs every 5 mins)  
│ ├── fetch_data.py ← Fetches data from Binance API  
│ ├── db_manager.py ← Handles database connection  
│ ├── logger.py ← Logs activity to log file  
│ └── ...other modules  
│  
├── data/  
│ └── market_data.db ← SQLite database storing price and volume  
│  
├── logs/  
│ └── daily_log.txt ← Log file (auto-generated)  
│  
├── frontend/  
│ ├── app.py ← Flask app to show dashboard  
│ ├── templates/  
│ │ └── dashboard.html ← HTML layout for dashboard  
│ └── static/  
│ └── style.css ← Styling  
│  
├── requirements.txt ← All dependencies  
└── README.md ← You're here!  


---

## ⚙️ Prerequisites

- Python 3.10+ installed
- Git installed
- Recommended: VS Code

---

## 🛠️ Installation Steps

```bash
# 1. Clone the repo
git clone https://github.com/badalrai21/Python-market-tracker.git
cd Python-market-tracker

# 2. Install required Python packages
pip install -r requirements.txt
```

## 🚀 How to Use

  1. Start the Tracker
  This will fetch and store real-time data every 5 minutes:
  
```
  # In project root
  PYTHONPATH=. python -m tracker.main
```
  The data will be saved in data/market_data.db.
  
  2. Run the Dashboard
  To visualize data in a web browser:
  
 ```
  # In project root
  cd frontend
  python app.py
```
  Then open: http://127.0.0.1:5000

## 🧪 Example Output

  [DATA] 2025-07-04T11:12:11 | BTCUSDT | Price: 109144.9 | Volume: 12574.08991

##  🧾 License
This project is licensed under the MIT License.



