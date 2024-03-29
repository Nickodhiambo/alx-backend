#!/usr/bin/env python3
"""Implements a simple pagination"""

import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """Returns a tuple containing start and end indices for a
    paginantion operation
    """
    start_index = (page - 1) * page_size
    end_index = (start_index + page_size)
    paginated_subset = (start_index, end_index)
    return paginated_subset


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
        """Implements a simple pagination"""
        assert type(page) == int and type(page_size) == int\
            and page > 0 and page_size > 0
        start, end = index_range(page, page_size)
        try:
            self.dataset()
            return self.__dataset[start:end]
        except IndexError:
            return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Returns hypermedia metadata in the response"""
        assert type(page) == int and type(page_size) == int\
            and page > 0 and page_size > 0
        my_dict = {}
        my_dict["page"] = page
        my_dict["data"] = self.get_page(page, page_size)
        my_dict["page_size"] = len(my_dict["data"])
        my_dict["next_page"] = page + 1 if self.get_page(page + 1, page_size)\
            else None
        my_dict["prev_page"] = page - 1 if page > 1 else None
        my_dict["total_pages"] = math.ceil(len(self.dataset()) / page_size)

        return my_dict
