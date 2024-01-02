#!/usr/bin/env python3
"""
The `0-basic_cache` module supplies a class `BasicCache` that
inherits from `BaseCaching`

Create a class BasicCache that inherits from BaseCaching and
is a caching system:

You must use self.cache_data - dictionary from the parent class
BaseCaching
This caching system doesn’t have limit
def put(self, key, item):
Must assign to the dictionary self.cache_data the item value for
the key key.
If key or item is None, this method should not do anything.
def get(self, key):
Must return the value in self.cache_data linked to key.
If key is None or if the key doesn’t exist in self.cache_data,
return None.
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache class """
    def __init__(self):
        # Calls the init method of the super/parent class
        super().__init__()

    def put(self, key, item):
        """ Adds an item to the cach_data key """
        if key is None or item is None:
            pass
        self.cache_data[key] = item

    def get(self, key):
        """ Returns the item associated with a key in cache_data """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)
