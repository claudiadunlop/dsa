"""Heap sort algorithm."""

from typing import TypeVar, List

T = TypeVar('T')


def heap_sort(data: List[T]) -> None:
    """Sort the list in place using heap sort.

    Heap sort builds a max-heap from the data, then repeatedly extracts
    the maximum element and places it at the end of the sorted portion.

    Time complexity: O(n log n) in all cases
    Space complexity: O(1)
    Stable: No

    Args:
        data: The list to sort in place.
    """
    n = len(data)
    if n < 2:
        return

    _build_max_heap(data)

    for end in range(n - 1, 0, -1):
        data[0], data[end] = data[end], data[0]
        _heapify(data, end, 0)
    
    #raise NotImplementedError


def _heapify(data: List[T], n: int, i: int) -> None:
    """Restore the max-heap property for subtree rooted at index i.

    Assumes the subtrees rooted at left(i) and right(i) are max-heaps.

    Args:
        data: The list representing the heap.
        n: The size of the heap (only indices 0 to n-1 are in the heap).
        i: The index of the root of the subtree to heapify.
    """
    while True:
        left = 2 * i + 1
        right = 2 * i + 2
        largest = i

        if left < n and data[left] > data[largest]:
            largest = left
        if right < n and data[right] > data[largest]:
            largest = right

        if largest == i:
            break

        data[i], data[largest] = data[largest], data[i]
        i = largest
        #raise NotImplementedError


def _build_max_heap(data: List[T]) -> None:
    """Convert the list into a max-heap in-place.

    Args:
        data: The list to convert to a max-heap.
    """
    n = len(data)
    for i in range(n // 2 - 1, -1, -1):
        _heapify(data, n, i)
    #raise NotImplementedError
