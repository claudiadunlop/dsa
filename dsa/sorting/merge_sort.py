"""Merge sort algorithm."""

from typing import TypeVar, List

T = TypeVar('T')


def merge_sort(data: List[T]) -> None:
    """Sort the list in place using merge sort.

    Merge sort is a divide-and-conquer algorithm that divides the list
    into halves, recursively sorts each half, and then merges the sorted
    halves back together.

    Time complexity: O(n log n) in all cases
    Space complexity: O(n) for the auxiliary array
    Stable: Yes

    Args:
        data: The list to sort in place.
    """
    raise NotImplementedError


def _merge(data: List[T], left: int, mid: int, right: int) -> None:
    """Merge two sorted subarrays data[left:mid+1] and data[mid+1:right+1].

    Args:
        data: The list containing the subarrays.
        left: Starting index of the first subarray.
        mid: Ending index of the first subarray.
        right: Ending index of the second subarray.
    """
    raise NotImplementedError
