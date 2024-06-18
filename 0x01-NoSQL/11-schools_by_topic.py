#!/usr/bin/env python3
"""Module that defines schools_by_topic function
"""


def schools_by_topic(mongo_collection, topic):
    """Selects school by a topic"""

    docs = []

    coll_docs = mongo_collection.find()

    for doc in coll_docs:
        print(doc)
        if 'topics' in doc.keys() and topic in doc['topics']:
            docs.append(doc)

    return docs
