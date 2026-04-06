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
    blockSize = 1
    while blockSize < len(data):
        for i in range(0, len(data), 2 * blockSize):
            mid = min(i + blockSize-1, len(data)-1)
            right = min(i+2 *blockSize-1, len(data) - 1)
            _merge(data, i, mid, right)
        blockSize *= 2
    return data

    #raise NotImplementedError


def _merge(data: List[T], left: int, mid: int, right: int) -> None:
    """Merge two sorted subarrays data[left:mid+1] and data[mid+1:right+1].

    Args:
        data: The list containing the subarrays.
        left: Starting index of the first subarray.
        mid: Ending index of the first subarray.
        right: Ending index of the second subarray.
    """
    i = left
    j = mid+1
    new_data = []

    while i<= mid and j <= right:
        if data[i] > data[j]:
            new_data.append(data[j])
            j += 1
        else:
            new_data.append(data[i])
            i += 1

    while i <= mid:
        new_data.append(data[i])
        i += 1

    while j <= right:
        new_data.append(data[j])
        j += 1

    for k in range(len(new_data)):
        data[left + k] = new_data[k]

    return new_data
    
    #raise NotImplementedError


