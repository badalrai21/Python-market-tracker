# tracker/logger.py

from .config import LOG_PATH

def log_message(message):
    with open(LOG_PATH, "a") as file:
        file.write(message + "\n")
    print(message)
