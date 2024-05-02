#!/usr/bin/env python3
"""get_page that takes two integer arguments page with default
value 1 and page_size with default value 10."""

import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initialize instance."""
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

    def index_range(page, page_size):
        """return a tuple of size two containing a start index
        and an end index corresponding to the range of indexes to return in
        a list for those particular pagination parameters."""
        start_index = (page - 1) * page_size
        end_index = start_index + page_size
        return start_index, end_index

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Get a specific page from the dataset."""
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0

        indices = self.index_range(page, page_size)
        start = indices[0]
        end = indices[1]

        try:
            return self.dataset()[start:end]
        except IndexError:
            return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """Implement a get_hyper method that takes the same arguments
        (and defaults) as get_page and returns a dictionary"""
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)
        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": (
                page + 1 if len(data) ==
                page_size and page < total_pages else None
            ),
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages,
        }
