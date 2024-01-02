#!/usr/bin/env python3
""" The `3-hypermedia_del_pagination` module """


def get_hyper_index(self, index: int = None,
                    page_size: int = 10) -> Dict:
    """ return all data"""
    if index is None:
        index = 0

    # validate the index
    assert isinstance(index, int)
    assert 0 <= index < len(self.indexed_dataset())
    assert isinstance(page_size, int) and page_size > 0

    data = []  # collect all indexed data
    next_index = index + page_size

    for value in range(index, next_index):
        if self.indexed_dataset().get(value):
            data.append(self.indexed_dataset()[value])
        else:
            value += 1
            next_index += 1

    return {
        'index': index,
        'data': data,
        'page_size': page_size,
        'next_index': next_index
        }
