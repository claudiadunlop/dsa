"""Quick sort algorithm."""

from typing import TypeVar, List
import random

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
    _quick_sort_range(data, 0, len(data)-1)

    #raise NotImplementedError


def _quick_sort_range(data: List[T], low: int, high: int) -> None:
    """Sort the subarray data[low:high+1] using quick sort.

    Args:
        data: The list containing the subarray.
        low: Starting index of the subarray.
        high: Ending index of the subarray.
    """
    if low >= high:
        return
    mid = _partition(data, low, high)
    _quick_sort_range(data, low, mid-1)
    _quick_sort_range(data, mid+1, high)

    #raise NotImplementedError


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
    pivot = random.randint(low, high)
    left = low + 1
    right = high
    
    temp = data[pivot]
    data[pivot] = data[low]
    data[low] = temp

    while left <= right:
        if data[left] > data[low] and data[right] < data[low]:
            temp = data[left]
            data[left] = data[right]
            data[right] = temp
            left += 1
            right -= 1
        elif data[left] > data[low]:
            right -= 1
        elif data[right] <= data[low]:
            left += 1
        else:
            left += 1
            right -= 1
        
    temp = data[low]
    data[low] = data[right]
    data[right] = temp

    return right

    #raise NotImplementedError

if __name__ == "__main__":
    data = [2, 7, 9, 11, 1, 3, 4, 8, 5, 6]
    print(_partition(data, 0, len(data)-1))
    print(data)