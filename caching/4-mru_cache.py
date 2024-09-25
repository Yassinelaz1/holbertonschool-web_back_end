#!/usr/bin/python3
"""MRU Caching"""

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """MRU Caching"""
    def __init__(self):
        """Initialize the class and call the parent class init"""
        super().__init__()
        self.mru_key = None  # Track the most recently used key

    def put(self, key, item):
        """Assign item to the dictionary with MRU eviction policy"""
        if key is None or item is None:
            return

        # If key already exists, update it but do not count it as a new put
        if key in self.cache_data:
            self.cache_data[key] = item
        else:
            # If cache is full, discard the most recently used item
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                if self.mru_key is not None:
                    print(f"DISCARD: {self.mru_key}")
                    del self.cache_data[self.mru_key]

            # Add new item to cache
            self.cache_data[key] = item

        # Update the most recently used key
        self.mru_key = key

    def get(self, key):
        """Return the value in cache linked to key,
        or None if key is not present"""
        if key is None or key not in self.cache_data:
            return None

        # Update the most recently used key
        self.mru_key = key
        return self.cache_data[key]
