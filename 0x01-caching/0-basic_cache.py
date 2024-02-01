#!/usr/bin/env python3
"""Contains a class 'BasicCache' that inherits from
'BaseCaching' and implements a simple GET/PUT methods
"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """Implements simple Get/Put methods"""
    def put(self, key, item):
        """Saves an item to cache by key"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Retrieves an item by key"""
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
