from pymongo import MongoClient


def create_db():
    client = MongoClient('mongodb://localhost:27017')
    db = client['fashion']
    return db.fashion

fashion_data = create_db()

def insert_db(fashion_input):
    fashion_data.insert_one(fashion_input)
