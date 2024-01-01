#!/usr/bin/env python3
""" The `0-simple_helper_function` module supplies a function `index_range` """
import csv
import math
from typing import Tuple
from typing import List


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

        data_list = self.dataset()
        try:
            start_index, stop_index = index_range(page, page_size)
            return data_list[start_index, stop_index]
        except IndexError:
            return []
