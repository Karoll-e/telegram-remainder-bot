import os
import urllib.parse

from pymongo.mongo_client import MongoClient

from logger_config import log


# Database setup
def connect_to_mongodb():
    try:
        username = os.environ.get("DATABASE_USERNAME")
        password = os.environ.get("DATABASE_PASSWORD")
        dbname = os.environ.get("DATABASE_NAME")
        collectionname = os.environ.get("DATABASE_COLLECTION_NAME")

        if not all([username, password, dbname, collectionname]):
            raise ValueError("Missing environment variables")

        password = urllib.parse.quote(password)
        uri = f"mongodb+srv://{username}:{password}@kuzco.2ktfafc.mongodb.net/?retryWrites=true&w=majority&appName=kuzco"
        client = MongoClient(uri)
        client.server_info()
        db = client[dbname][collectionname]
        return db
    except Exception as e:
        log.error("Error connecting to the database:", e)
        return None


db = connect_to_mongodb()
if db is not None:
    log.info("Connection to the database and collection successful.")
else:
    log.error("Failed to establish connection.")
