#!/usr/bin/env python3
"""Module that defines list_all function
"""
from pymongo import MongoClient


def list_all(mongo_collection):
    """Lists all documents in mongo_collection"""
    docs = []

    coll_docs = mongo_collection.find()

    for doc in coll_docs:
        docs.append(doc)

    return docs
