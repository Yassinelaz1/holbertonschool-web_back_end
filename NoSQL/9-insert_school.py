#!/usr/bin/env python3
"""Python function that inserts a new document in a collection
based on kwargs"""


def insert_school(mongo_collection, **kwargs):
    """
    Insert a new document in a collection based on kwargs
    """
    collection = mongo_collection.insert_one(kwargs)
    return collection.inserted_id
