#!/usr/bin/python3
"""Contains a class that implements a FIFO caching mechanism"""


BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """Implements a FIFO cache"""
    def __init__(self) -> None:
        super().__init__()

    def put(self, key, item):
        """Inserts an item to dict by key"""
        if key is not None and item is not None:
            if len(self.cache_data) == self.MAX_ITEMS\
                    and key not in self.cache_data.keys():
                key_to_discard = list(self.cache_data.keys())[0]
                del self.cache_data[key_to_discard]
                print(f"DISCARD: {key_to_discard}")
            self.cache_data[key] = item

    def get(self, key):
        """Retrieves an item by key"""
        if key is not None and key in self.cache_data.keys():
            return self.cache_data[key]
        return None
