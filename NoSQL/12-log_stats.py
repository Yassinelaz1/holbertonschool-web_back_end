#!/usr/bin/env python3
"""Python script that provides some stats about Nginx logs
stored in MongoDB:"""

from pymongo import MongoClient


list_all = __import__("8-all").list_all

if __name__ == "__main__":
    client = MongoClient("mongodb://127.0.0.1:27017")
    collection = client.logs.nginx
    logs = collection.count_documents({})
    print("{} logs".format(logs))
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")
    count = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{count} status check")
