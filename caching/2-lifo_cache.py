#!/usr/bin/python3
"""LIFO Caching"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """LIFO Caching"""
    def __init__(self):
        """Initialize the class and call the parent class init"""
        super().__init__()
        self.last_key = None

    def put(self, key, item):
        """Assign item to the dictionary with LIFO eviction policy"""
        b = BaseCaching.MAX_ITEMS
        if key is None or item is None:
            return
        if len(
                self.cache_data) >= b and key not in self.cache_data:
            if self.last_key is not None:
                print(f"DISCARD: {self.last_key}")
                del self.cache_data[self.last_key]
        self.cache_data[key] = item
        self.last_key = key

    def get(self, key):
        """Return the value in cache linked to key,
        or None if key is not present"""
        return self.cache_data.get(key, None)
