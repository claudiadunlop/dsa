"""Binary heap implementation of a priority queue."""

from dsa.priority_queues.base import PriorityQueue
from typing import TypeVar, Tuple, List

K = TypeVar('K')
V = TypeVar('V')


class Heap(PriorityQueue[K, V]):
    """Priority queue implementation using a binary heap.

    A binary heap is a complete binary tree stored in an array where
    each node's key is less than or equal to its children's keys
    (min-heap property).

    Array representation:
        - Root is at index 0
        - For node at index i:
            - Parent is at (i - 1) // 2
            - Left child is at 2 * i + 1
            - Right child is at 2 * i + 2
    """

    def __init__(self):
        """Create an empty heap."""
        raise NotImplementedError

    def __len__(self) -> int:
        raise NotImplementedError

    def add(self, key: K, value: V) -> None:
        raise NotImplementedError

    def min(self) -> Tuple[K, V]:
        raise NotImplementedError

    def remove_min(self) -> Tuple[K, V]:
        raise NotImplementedError

    def _parent(self, i: int) -> int:
        """Return the index of the parent of index i."""
        raise NotImplementedError

    def _left(self, i: int) -> int:
        """Return the index of the left child of index i."""
        raise NotImplementedError

    def _right(self, i: int) -> int:
        """Return the index of the right child of index i."""
        raise NotImplementedError

    def _has_left(self, i: int) -> bool:
        """Return True if index i has a left child."""
        raise NotImplementedError

    def _has_right(self, i: int) -> bool:
        """Return True if index i has a right child."""
        raise NotImplementedError

    def _swap(self, i: int, j: int) -> None:
        """Swap the elements at indices i and j."""
        raise NotImplementedError

    def _upheap(self, i: int) -> None:
        """Move the element at index i up to restore heap property."""
        raise NotImplementedError

    def _downheap(self, i: int) -> None:
        """Move the element at index i down to restore heap property."""
        raise NotImplementedError
