#!/usr/bin/env python3
"""Python script that provides some stats about Nginx logs
stored in MongoDB:"""

from pymongo import MongoClient


def get_nginx_stats(db):
    """provides some stats about Nginx logs stored in MongoDB"""
    collection = db["nginx"]
    logs = collection.count_documents({})
    print(f"{logs} logs")
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for i in methods:
        count = collection.count_documents({"method": i})
        print(f"\tmethod {i}: {count}")
    status = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status} status check")


if __name__ == "__main__":
    client = MongoClient("mongodb://localhost:27017/")
    db = client["logs"]
