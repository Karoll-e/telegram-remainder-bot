import os

# ENV = "DEV"
ENV = "PROD"


## keys
if ENV == "DEV":
    telegram_key = os.environ.get("TELEGRAM_KEY")
    mongodb_key = os.environ.get("DATABASE_PASSWORD")
elif ENV == "PROD":
    import ast

    telegram_key = os.environ.get("TELEGRAM_KEY")
    mongodb_key = os.environ.get("DATABASE_PASSWORD")


## server
host = "0.0.0.0"
port = int(os.environ.get("PORT", 5000))
webhook = "https://telegram-remainder-bot.onrender.com"


## fs
# root = os.path.dirname(os.path.dirname(__file__)) + "/"
