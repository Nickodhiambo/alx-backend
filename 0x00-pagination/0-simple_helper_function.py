#!/usr/bin/env python3
"""A function that takes page size and number and returns a tuple
containing start and end indices for a pagination operation"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """Returns a tuple containing start and end indices for a
    paginantion operation
    """
    start_index = (page - 1) * page_size
    end_index = (start_index + page_size)
    paginated_subset = (start_index, end_index)
    return paginated_subset
