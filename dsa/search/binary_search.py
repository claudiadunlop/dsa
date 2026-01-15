"""Binary search algorithm."""

from typing import TypeVar, List, Optional

T = TypeVar('T')


def binary_search(data: List[T], target: T) -> Optional[int]:
    """Search for target in a sorted list using binary search.

    Binary search repeatedly divides the search interval in half.
    If the target value is less than the middle element, the search
    continues in the lower half; otherwise, it continues in the upper half.

    Time complexity: O(log n)
    Space complexity: O(1)

    Args:
        data: A sorted list to search.
        target: The value to search for.

    Returns:
        The index of target if found, None otherwise.
    """
    raise NotImplementedError


def binary_search_recursive(data: List[T], target: T) -> Optional[int]:
    """Search for target in a sorted list using recursive binary search.

    This is the recursive implementation of binary search.

    Time complexity: O(log n)
    Space complexity: O(log n) due to recursion stack

    Args:
        data: A sorted list to search.
        target: The value to search for.

    Returns:
        The index of target if found, None otherwise.
    """
    raise NotImplementedError


def _binary_search_helper(data: List[T], target: T, low: int, high: int) -> Optional[int]:
    """Recursive helper for binary search.

    Args:
        data: A sorted list to search.
        target: The value to search for.
        low: The lower bound of the search range (inclusive).
        high: The upper bound of the search range (inclusive).

    Returns:
        The index of target if found, None otherwise.
    """
    raise NotImplementedError


def bisect_left(data: List[T], target: T) -> int:
    """Find the leftmost insertion point for target in a sorted list.

    Returns the index where target should be inserted to maintain sorted order.
    If target is already present, the insertion point is before (to the left of)
    any existing entries.

    Time complexity: O(log n)
    Space complexity: O(1)

    Args:
        data: A sorted list.
        target: The value to find the insertion point for.

    Returns:
        The leftmost index where target can be inserted.
    """
    raise NotImplementedError


def bisect_right(data: List[T], target: T) -> int:
    """Find the rightmost insertion point for target in a sorted list.

    Returns the index where target should be inserted to maintain sorted order.
    If target is already present, the insertion point is after (to the right of)
    any existing entries.

    Time complexity: O(log n)
    Space complexity: O(1)

    Args:
        data: A sorted list.
        target: The value to find the insertion point for.

    Returns:
        The rightmost index where target can be inserted.
    """
    raise NotImplementedError
