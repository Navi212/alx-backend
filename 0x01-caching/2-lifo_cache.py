#!/usr/bin/env python3
"""
The `2-lifo_cache` mudule supplies a class `LIFOCache` that
inherits from `BaseCaching`.

LIFO Caching:
Create a class LIFOCache that inherits from BaseCaching and
is a caching system:

You must use self.cache_data - dictionary from the parent
class BaseCaching
You can overload def __init__(self): but don’t forget to call
the parent init: super().__init__()
def put(self, key, item):
Must assign to the dictionary self.cache_data the item value
for the key key.
If key or item is None, this method should not do anything.
If the number of items in self.cache_data is higher that
BaseCaching.MAX_ITEMS:
you must discard the last item put in cache (LIFO algorithm)
you must print DISCARD: with the key discarded and following
by a new line
def get(self, key):
Must return the value in self.cache_data linked to key.
If key is None or if the key doesn’t exist in self.cache_data,
return None.
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ defines a class LIFOCache """
    def __init__(self):
        # Calls the init method of the super/parent class
        super().__init__()

    def put(self, key, item):
        """ Removes the last key from the cache_data dict """
        if key is None or item is None:
            pass
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS \
                    and key not in self.cache_data.keys():
                del_key, _ = self.cache_data.popitem()
                print(f"DISCARD: {del_key}")
            self.cache_data[key] = item

    def get(self, key):
        """ Returns the item associated with a key in cache_data """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)
