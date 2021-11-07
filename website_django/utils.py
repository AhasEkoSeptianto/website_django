from pymongo import MongoClient


def get_db_handle(db_name, host, port, username, password):
    client = MongoClient(
        host=host,
        port=port,
        username=username,
        password=password
    )

    db_handle = client['db_name']
    return db_handle, client