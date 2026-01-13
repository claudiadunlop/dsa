"""Quick sort algorithm."""

from typing import TypeVar, List

T = TypeVar('T')


def quick_sort(data: List[T]) -> None:
    """Sort the list in place using quick sort.

    Quick sort is a divide-and-conquer algorithm that selects a pivot
    element, partitions the list around the pivot (elements less than
    pivot on left, greater on right), and recursively sorts the partitions.

    Time complexity: O(n log n) average case, O(n^2) worst case
    Space complexity: O(log n) average case for recursion stack
    Stable: No

    Args:
        data: The list to sort in place.
    """
    raise NotImplementedError


def _quick_sort_range(data: List[T], low: int, high: int) -> None:
    """Sort the subarray data[low:high+1] using quick sort.

    Args:
        data: The list containing the subarray.
        low: Starting index of the subarray.
        high: Ending index of the subarray.
    """
    raise NotImplementedError


def _partition(data: List[T], low: int, high: int) -> int:
    """Partition the subarray around a pivot.

    Rearranges elements so that all elements less than the pivot come
    before it, and all elements greater come after it.

    Args:
        data: The list containing the subarray.
        low: Starting index of the subarray.
        high: Ending index of the subarray.

    Returns:
        The final index of the pivot element.
    """
    raise NotImplementedError
