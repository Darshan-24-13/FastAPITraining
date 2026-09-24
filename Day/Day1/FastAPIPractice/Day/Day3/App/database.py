from pymongo import MongoClient

from .config import settings

client = MongoClient(settings.MONGO_URI)

db = client[settings.MONGO_DB_NAME]


def ping_database():
    try:
        client.admin.command("ping")
        return True
    except Exception:
        return False