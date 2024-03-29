#!/usr/bin/env python3
"""A class that implements LFU Caching"""
BaseCaching = __import__("base_caching").BaseCaching


class LFUCache(BaseCaching):
    """Implements LFU Caching"""
    def __init__(self) -> None:
        super().__init__()
        self.__access = {}

    def put(self, key, item):
        """Add an item to the cache"""
        if key is not None and item is not None:
            if len(self.cache_data) == self.MAX_ITEMS\
                    and key not in self.cache_data.keys():
                key_to_discard = self.get_lrk()
                del self.cache_data[key_to_discard]
                del self.__access[key_to_discard]
                print(f"DISCARD: {key_to_discard}")
            if key not in self.cache_data:
                self.__access[key] = 0
            else:
                self.__access[key] += 1
            self.cache_data[key] = item

    def get(self, key):
        """Get an item by key"""
        if key is not None and key in self.cache_data:
            if key in self.__access:
                self.__access[key] += 1
            return self.cache_data[key]
        return None

    def get_lrk(self):
        """Get the least requested key"""
        keys = list(self.__access.keys())
        # print(self.__access)
        lrk = 0
        # print(keys)
        for i in range(1, len(keys)):
            if self.__access[keys[lrk]] > self.__access[keys[i]]:
                lrk = i
        return keys[lrk]
