#!/usr/bin/env python3
"""Module that defines insert_school function
"""
from pymongo import MongoClient


def insert_school(mongo_collection, **kwargs):
    """Inserts documents in the mongo_collection"""

    new_doc = mongo_collection.insert_one(kwargs)

    return (new_doc.inserted_id)
