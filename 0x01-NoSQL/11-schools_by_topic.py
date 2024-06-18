#!/usr/bin/env python3
"""Module that defines schools_by_topic function
"""


def schools_by_topic(mongo_collection, topic):
    """Selects school by a topic"""

    docs = []

    coll_docs = mongo_collection.find({'topics': topic})

    for doc in coll_docs:
        docs.append(doc)

    return docs
