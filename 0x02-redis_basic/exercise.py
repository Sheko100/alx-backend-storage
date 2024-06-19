#!/usr/bin/env python3
"""Module that defines the Cache class
"""
import redis
from typing import Union
from uuid import uuid4


class Cache:

    def __init__(self) -> None:
        """Initializes the instance"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Stores the data in redis with a new random key

        Args:
            data: the data to store

        Returns:
            new_key (str): the new key
        """
        new_key = str(uuid4())
        self._redis.set(new_key, data)

        return new_key
