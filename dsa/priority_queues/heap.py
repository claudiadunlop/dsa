"""Binary heap implementation of a priority queue."""

from dsa.priority_queues.base import PriorityQueue
from typing import TypeVar, Tuple, List
from dsa.lists import ArrayList

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
    
    class item:
        def __init__(self, key, value):
            self._key = key
            self._value = value

    def __init__(self):
        """Create an empty heap."""
        self._data = ArrayList()
        self._n = 0
        #raise NotImplementedError

    def __len__(self) -> int:
        return self._n
        #raise NotImplementedError

    def add(self, key: K, value: V) -> None:
        self._data.append(self.item(key,value))
        self._n +=1
        self._upheap(len(self._data) - 1)
        #raise NotImplementedError

    def min(self) -> Tuple[K, V]:
        item = self._data[0]
        return (item._key, item._value)
        #raise NotImplementedError

    def remove_min(self) -> Tuple[K, V]:
        if self._n == 0:
            raise IndexError
        self._swap(0, self._n - 1)
        min = self._data[self._n-1]
        del self._data[self._n-1]
        self._n -= 1
        self._downheap(0)
        return (min._key, min._value)

        
        #raise NotImplementedError

    def _parent(self, i: int) -> int:
        """Return the index of the parent of index i."""
        return (i -1)//2
        #raise NotImplementedError

    def _left(self, i: int) -> int:
        """Return the index of the left child of index i."""
        return 2 * i + 1
        #raise NotImplementedError

    def _right(self, i: int) -> int:
        """Return the index of the right child of index i."""
        return 2 * i + 2
        # raise NotImplementedError

    def _has_left(self, i: int) -> bool:
        """Return True if index i has a left child."""
        if len(self._data) > 2 * i + 1:
            return True
        #raise NotImplementedError

    def _has_right(self, i: int) -> bool:
        """Return True if index i has a right child."""
        if len(self._data) > 2 * i + 2:
            return True
        #raise NotImplementedError

    def _swap(self, i: int, j: int) -> None:
        """Swap the elements at indices i and j."""
        temp = self._data[i]
        self._data[i] = self._data[j]
        self._data[j] = temp
        #raise NotImplementedError

    def _upheap(self, i: int) -> None:
        """Move the element at index i up to restore heap property."""
        while i > 0 and self._data[i]._key < self._data[self._parent(i)]._key:
            self._swap(i, self._parent(i))
            i = self._parent(i)
        #raise NotImplementedError

    def _downheap(self, i: int) -> None:
        """Move the element at index i down to restore heap property."""
        while self._has_left(i):
            left = self._left(i)
            smaller = left
            if self._has_right(i):
                right = self._right(i)
                if self._data[right]._key < self._data[left]._key:
                    smaller = right
            if self._data[smaller]._key < self._data[i]._key:
                self._swap(i, smaller)
                i = smaller
            else:
                break
        #raise NotImplementedError
