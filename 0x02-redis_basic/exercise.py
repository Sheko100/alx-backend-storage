#!/usr/bin/env python3
"""Module that defines the Cache class
"""
from functools import wraps
import redis
from typing import Union, Callable, List
from uuid import uuid4


def replay(method: Callable) -> None:
    """Prints how the method is used"""
    name = method.__qualname__
    instance = method.__self__
    called_times = instance.get_int(name)
    print("{} was called {} times".format(name, called_times))
    inputs = instance._redis.lrange("{}:inputs".format(name), 0, -1)
    outputs = instance._redis.lrange("{}:outputs".format(name), 0, -1)
    for ele in zip(inputs, outputs):
        print("{}(*{}) -> {}".format(
            name, ele[0].decode(), ele[1].decode()))


def call_history(method: Callable) -> Callable:
    """Decorator function that stores methods inputs and outputs
    in a list in redis
    """
    name = method.__qualname__
    in_key = "{}:inputs".format(name)
    out_key = "{}:outputs".format(name)

    @wraps(method)
    def wrapper(self, *args):
        str_args = str(args)
        self._redis.rpush(in_key, str_args)
        out = method(self, *args)
        self._redis.rpush(out_key, out)

        return out

    return wrapper


def count_calls(method: Callable) -> Callable:
    """Decorator function that count the methods calls
    """
    @wraps(method)
    def wrapper(self, data):
        self._redis.incr(method.__qualname__, 1)

    return wrapper


class Cache:

    def __init__(self) -> None:
        """Initializes the instance"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Stores the data in redis with a new random key

        Args:
            data: the data to store

        Returns:
            new_key (str): the new key
        """
        new_key = str(uuid4())
        if data:
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
