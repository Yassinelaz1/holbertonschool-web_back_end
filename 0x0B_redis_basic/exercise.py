#!/usr/bin/env python3
"""
Redis Cache Module
"""

import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """Decorator to count how many times a method is called.
    Increments a counter in Redis every time the method is called. """

    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ Wrapper for decorator functionality """
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    """ Decorator to store the input and output history of a function in Redis.
    It appends input arguments to a ':inputs' list
    and output to a ':outputs' list.
    """

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ Wrapper for decorator functionality """
        input = str(args)
        key = method.__qualname__
        self._redis.rpush(f"{key}:inputs", input)

        result = str(method(self, *args, **kwargs))
        self._redis.rpush(f"{key}:outputs", result)

        return result

    return wrapper


def replay(fn: Callable) -> None:
    """
    Display the history of calls to a particular function.
    """
    try:
        n_calls = redis.Redis.get(fn.__qualname__)
    except Exception:
        n_calls = 0
    print(f'{fn.__qualname__} was called {n_calls} times:')

    ins = redis.Redis().lrange(fn.__qualname__ + ":inputs", 0, -1)
    outs = redis.Redis().lrange(fn.__qualname__ + ":outputs", 0, -1)

    for a, b in zip(ins, outs):
        try:
            a = a.decode('utf-8')
        except Exception:
            a = ""
        try:
            b = b.decode('utf-8')
        except Exception:
            b = ""

        print(f'{fn.__qualname__}(*{a}) -> {b}')


class Cache:
    """Cache class for storing data in Redis."""

    def __init__(self):
        """Initialize the Redis client and flush the database."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store data in Redis with a randomly generated key.

        Args:
            data (Union[str, bytes, int, float]): The data to store in Redis.

        Returns:
            str: The generated key used to store the data.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self,
            key: str,
            fn: Optional[Callable] = None) -> Union[str,
                                                    bytes,
                                                    int,
                                                    float,
                                                    None]:
        """
        Retrieve data from Redis and optionally apply a conversion function."""
        data = self._redis.get(key)
        if data is None:
            return None
        return fn(data) if fn else data

    def get_str(self, key: str) -> Optional[str]:
        """
        Retrieve a string from Redis."""
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        """Retrieve an integer from Redis."""
        return self.get(key, fn=int)
