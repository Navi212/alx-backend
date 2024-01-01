#!/usr/bin/env python3
""" The `0-simple_helper_function` module supplies a function `index_range` """
from typing import Tuple


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
