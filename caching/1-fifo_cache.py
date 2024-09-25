#!/usr/bin/python3
"""1. FIFO caching"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    def __init__(self):
        """Initialize the class and call the parent class init"""
        super().__init__()
        self.order = []  # To maintain the order of keys

    def put(self, key, item):
        """Assign item to the dictionary with FIFO eviction policy"""
        if key is None or item is None:
            return

        """If key already exists, update the value and reorder"""
        if key in self.cache_data:
            self.order.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            """ If cache is full, discard the first item (FIFO)"""
            first_key = self.order.pop(0)
            del self.cache_data[first_key]
            print(f"DISCARD: {first_key}")

        """Add new item"""
        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """Return the value in cache linked to key,
        or None if key is not present"""
        return self.cache_data.get(key, None)
