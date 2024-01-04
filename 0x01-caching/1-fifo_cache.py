#!/usr/bin/env python3
"""
The `1-fifo_cache` mudule supplies a class `FIFOCache` that
inherits from `BaseCaching`.

FIFO Caching:
Create a class FIFOCache that inherits from BaseCaching
and is a caching system:

You must use self.cache_data - dictionary from the parent
class BaseCaching
You can overload def __init__(self): but don’t forget to \
call the parent init: super().__init__()
def put(self, key, item):
Must assign to the dictionary self.cache_data the item value
for the key key.
If key or item is None, this method should not do anything.
If the number of items in self.cache_data is higher that
BaseCaching.MAX_ITEMS: you must discard the first item put
in cache (FIFO algorithm) you must print DISCARD: with the
key discarded and following by a new line
def get(self, key):
Must return the value in self.cache_data linked to key.
If key is None or if the key doesn’t exist in self.cache_data,
return None.
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ defines a class FIFOCache """
    def __init__(self):
        # Calls the init method of the super/parent class
        super().__init__()

    def put(self, key, item):
        """ Adds an item to the cach_data key """
        if key is None or item is None:
            pass
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            del_key = next(iter(self.cache_data))
            del self.cache_data[del_key]
            print(f"DISCARD: {del_key}")
        else:
            self.cache_data[key] = item

    def get(self, key):
        """ Returns the item associated with a key in cache_data """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)
