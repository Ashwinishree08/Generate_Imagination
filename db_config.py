# imagination-sketch/db_config.py
import pymongo
import os
from dotenv import load_dotenv

load_dotenv()

def get_db():
    client = pymongo.MongoClient(os.getenv("MONGO_URI", "mongodb://localhost:27017/"))
    return client[os.getenv("DB_NAME", "imagination_sketch")]