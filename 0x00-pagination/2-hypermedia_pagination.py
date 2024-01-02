#!/usr/bin/env python3
""" The `2-hypermedia_pagination` module """
import csv
import math
from typing import Tuple, List, Dict


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    index_range: Function taking page and page_size params

    Args:
    page:        int
    page_size:   int

    Return:      Tuple of ints
    """
    start_index = (page - 1) * page_size
    stop_index = start_index + page_size
    return (start_index, stop_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Get page"""
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0

        # return a list of rows in the csv file named
        # DATA_FILE = "Popular_Baby_Names.csv"
        data_list = self.dataset()
        try:
            # Get the start and stop index
            start_index, stop_index = index_range(page, page_size)
            # Slice the data_list of rows from start_index to stop_index
            return data_list[start_index:stop_index]
        except IndexError:
            return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """returns a dictionary containing the following key-value pairs
        """
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0

        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)

        start, end = index_range(page, page_size)

        # estimating the next page
        if (page < total_pages):
            next_page = page+1
        else:
            next_page = None

        # estimating the previous page
        if (page == 1):
            prev_page = None
        else:
            prev_page = page - 1

        return {'page_size': len(data),
                'page': page,
                'data': data,
                'next_page': next_page,
                'prev_page': prev_page,
                'total_pages': total_pages
                }
