"""Elementary sorting algorithms."""

from typing import TypeVar, List

T = TypeVar('T')
 

def insertion_sort(data: List[T]) -> None:
    """Sort the list in place using insertion sort.

    Insertion sort builds the sorted list one element at a time by
    repeatedly taking the next element and inserting it into its
    correct position among the already-sorted elements.

    Time complexity: O(n^2) worst/average case, O(n) best case (nearly sorted)
    Space complexity: O(1)
    Stable: Yes

    Args:
        data: The list to sort in place.
    """
    
    for i in range(1, len(data)):
        temp = data[i]
        j = i-1
        while j >= 0 and temp < data[j]:
            data[j+1] = data[j]
            j -= 1
        data[j+1] = temp

    return data

    #raise NotImplementedError


def selection_sort(data: List[T]) -> None:
    """Sort the list in place using selection sort.

    Selection sort repeatedly finds the minimum element from the unsorted
    portion and swaps it with the first unsorted element.

    Time complexity: O(n^2) in all cases
    Space complexity: O(1)
    Stable: No (standard implementation)

    Args:
        data: The list to sort in place.
    """

    n = len(data)

    for i in range(n):
        min = i
        for j in range(i+1, n):
            if data[j] < data[min]:
                min = j
            
        temp = data[min]
        data[min] = data[i]
        data[i] = temp

    return data
    #raise NotImplementedError


def bubble_sort(data: List[T]) -> None:
    """Sort the list in place using bubble sort.

    Bubble sort repeatedly steps through the list, compares adjacent
    elements, and swaps them if they are in the wrong order. The pass
    through the list is repeated until the list is sorted.

    Time complexity: O(n^2) worst/average case, O(n) best case (already sorted)
    Space complexity: O(1)
    Stable: Yes

    Args:
        data: The list to sort in place.
    """
    
    for i in range(len(data)):
        for j in range(len(data) - 1):
            if data[j] > data[j + 1]:
                temp = data[j + 1]
                data[j + 1] = data[j]
                data[j] = temp


    #raise NotImplementedError
