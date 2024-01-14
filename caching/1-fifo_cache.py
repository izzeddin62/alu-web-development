#!/usr/bin/python3
"""fifo cache"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """fifo cache"""

    def put(self, key, item):
        """Add an item in the cache"""
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            discard = next(iter(self.cache_data))
            print("DISCARD: {}".format(discard))
            del self.cache_data[discard]
        self.cache_data[key] = item