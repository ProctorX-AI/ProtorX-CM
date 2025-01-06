from pymongo import MongoClient
from cm_protorX.settings import DATABASES

def get_db_handle(db_name, host, port, username, password):
    uri = f"mongodb://{username}:{password}@{host}:{port}/{db_name}"
    client = MongoClient(uri)
    db_handle = client['db_name']
    return db_handle, client

db_handle, client = get_db_handle(**DATABASES.get("default").get("CLIENT"))