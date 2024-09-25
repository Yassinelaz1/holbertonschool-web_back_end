#!/usr/bin/python3
"""LRU Caching"""

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """LRU Caching"""
    def __init__(self):
        """Initialize the class and call the parent class init"""
        super().__init__()
        self.lru_order = []  # To maintain the order of key usage

    def put(self, key, item):
        """Assign item to the dictionary with LRU eviction policy"""
        if key is None or item is None:
            return

        # If the key already exists, remove it from the LRU tracking list
        if key in self.cache_data:
            self.lru_order.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # If cache is full, discard the least recently used item (first in
            # list)
            lru_key = self.lru_order.pop(0)
            del self.cache_data[lru_key]
            print(f"DISCARD: {lru_key}")

        # Add the item to cache and update the usage order
        self.cache_data[key] = item
        self.lru_order.append(key)

    def get(self, key):
        """Return the value in cache linked to key,
        or None if key is not present"""
        if key is None or key not in self.cache_data:
            return None

        # Move the accessed key to the end of the list to mark it as recently
        # used
        self.lru_order.remove(key)
        self.lru_order.append(key)

        return self.cache_data.get(key)
