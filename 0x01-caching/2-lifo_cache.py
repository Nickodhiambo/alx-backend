#!/usr/bin/python3
"""A class that implements LIFO caching"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """Implements LIFO caching"""
    def __init__(self) -> None:
        super().__init__()

    def put(self, key, item):
        """Inserts items to cache by key"""
        if key is not None and item is not None:
            if len(self.cache_data) == self.MAX_ITEMS\
                    and key not in self.cache_data.keys():
                key_to_remove = list(self.cache_data.keys())[-1]
                del self.cache_data[key_to_remove]
                print(f"DISCARD: {key_to_remove}")
            self.cache_data[key] = item

    def get(self, key):
        """Retrieve item by key from cache"""
        if key is not None:
            return self.cache_data[key]
        return None
