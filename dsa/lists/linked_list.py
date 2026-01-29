"""Linked list implementation."""

from dsa.lists.base import Sequence
from typing import TypeVar, Iterator, Optional

T = TypeVar('T')


class LinkedList(Sequence[T]):
    """Sequence implementation using a doubly linked list.

    Each element is stored in a node containing the value and references
    to the previous and next nodes. Provides O(1) insertion/deletion at
    known positions but O(n) random access.
    """

    class _Node:
        """A node in the doubly linked list."""
        __slots__ = '_element', '_prev', '_next'

        def __init__(self, element: T, prev: Optional['LinkedList._Node'] = None,
                     next: Optional['LinkedList._Node'] = None):
            self._element = element
            self._prev = prev
            self._next = next

    def __init__(self):
        """Create an empty linked list."""
        self._head = None
        self._n = 0
        #raise NotImplementedError

    def append(self, value: T) -> None:
        if self._n == 0:
            self._head = self._Node(value, prev = None, next = None)
        else:
            current_node = self._head
            while current_node._next is not None:
                current_node = current_node._next
            current_node._next = self._Node(value, self._head, None)
        self._n += 1
        #raise NotImplementedError

    def __getitem__(self, index: int) -> T:
        if not 0 <= index < self._n:
            raise IndexError
        current_node = self._head
        for i in range(index):
            current_node = current_node._next
        return current_node._element
        #raise NotImplementedError

    def __setitem__(self, index: int, value: T) -> None:
        if not 0 <= index < self._n:
            raise IndexError
        current_node = self._head
        for i in range(index):
            current_node = current_node._next
        current_node._element = value
        #raise NotImplementedError

    def __delitem__(self, index: int) -> None:
        if not 0 <= index <= self._n:
            raise IndexError
        current_node = self._head
        for i in range(index):
            current_node = current_node._next
        if current_node._prev == None:
            current_node._next._prev = None
            self._head = current_node._next
        elif current_node._next == None:
            current_node._prev._next = None
        else:
            current_node._next._prev = current_node._prev
            current_node._prev._next = current_node._next
        self._n -= 1
        #raise NotImplementedError

    def insert(self, index: int, value: T) -> None:
        if not 0 <= index <= self._n:
            raise IndexError
        current_node = self._head
        if index == 0:
            new_node = self._Node(value, prev = None, next = current_node)
            current_node._prev = new_node
            self._head = new_node
            self._n += 1
            return
        for i in range(index-1):
            current_node = current_node._next
        new_node = self._Node(value, prev = current_node, next = current_node._next)
        current_node._next = new_node
        if new_node._next is not None:
            new_node._next._prev = new_node
        self._n += 1
        #raise NotImplementedError

    def __len__(self) -> int:
        return self._n
        #raise NotImplementedError

    def __iter__(self) -> Iterator[T]:
        for i in range(self._n):
            yield self[i]
        #raise NotImplementedError
