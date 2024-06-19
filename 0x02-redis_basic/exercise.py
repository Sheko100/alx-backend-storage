#!/usr/bin/env python3
"""Module that defines the Cache class
"""
import redis
from typing import Union, Callable, List
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

    def get(self, key: str, fn: Callable = None) -> Union[
            str, bytes, int, float, List]:
        """Retrieve a value based on key and converts its type using fn

        Args:
            key: key to retreive the value
            fn: Callabe to convert the retrieved value

        Returns:
            value: the retrieved value
        """
        value = self._redis.get(key)

        if value and fn:
            value = fn(value)

        return value

    def get_str(self, key: str) -> str:
        """Retrieves a string value based on the key

        Args:
            key: key associted with the value

        Returns:
            value = the string value
        """
        value = self.get(key, str)

        return value

    def get_int(self, key: str) -> int:
        """Retrieves an integer value based on the key

        Args:
            key: key associted with the value

        Returns:
            value = the integer value
        """
        value = self.get(key, int)

        return value
