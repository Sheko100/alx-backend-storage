#!/usr/bin/env python3
"""Module that defines update_topics function
"""
from pymongo import MongoClient


def update_topics(mongo_collection, name, topics):
    """Updates topics a school document based on the name"""

    update = mongo_collection.update_one(
            {'name': name},
            {'$set': {'topics': topics}}
            )
