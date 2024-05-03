#!/usr/bin/env python3
"""Python script that provides some stats about Nginx logs stored in MongoDB:"""

from pymongo import MongoClient

if __name__ == "__main__":
    """ provides some stats about Nginx logs stored in MongoDB
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx

    logs = collection.count_documents({})
    print(f'{logs} logs')
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print('Methods:')
    for x in methods:
        count = collection.count_documents({"method": x})
        print(f'\tmethod {x}: {count}')

    status_check = collection.count_documents(
        {"method": "GET", "path": "/status"}
        )
    print(f'{status_check} status check')
