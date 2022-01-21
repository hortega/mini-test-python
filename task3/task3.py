"""
Find the first recurring character of the below lists

Run
"""
from typing import Union, List

task3 = [
    [2, 5, 1, 2, 3, 5, 1, 2, 4],  # Should return 2
    [2, 1, 1, 2, 3, 5, 1, 2, 4],  # Should return 1
    [2, 3, 4, 5],  # Should return None
    [2, 5, 5, 2, 3, 5, 1, 2, 4]  # Should return 5
]


def _find_first_duplicate_in_list(lst: List[int]) -> Union[int, None]:
    buffer = set()
    for n in lst:
        if n in buffer:
            return n
        buffer.add(n)
    return None


def find_first_duplicate_in_lists(lists: List[List[int]]) -> None:
    for lst in lists:
        print(f'{lst}: {_find_first_duplicate_in_list(lst)}')

