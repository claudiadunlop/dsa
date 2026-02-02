"""Linked list-based queue implementation."""

from dsa.stacks_queues.base import Queue
from typing import TypeVar, Optional

T = TypeVar('T')


class LinkedQueue(Queue[T]):
    """Queue implementation using a singly linked list.

    Maintains pointers to both the head (front) and tail (back) of the
    list for O(1) enqueue and dequeue operations.
    """

    class _Node:
        """A node in the singly linked list."""
        __slots__ = '_element', '_next'

        def __init__(self, element: T, next: Optional['LinkedQueue._Node'] = None):
            self._element = element
            self._next = next

    def __init__(self):
        self._head = None
        self._n = 0
        #raise NotImplementedError

    def enqueue(self, item: T) -> None:
        if self._n == 0:
            self._head = self._Node(item, next = None)
        else:
            current_node = self._head
            while current_node._next is not None:
                    current_node = current_node._next
            current_node._next = self._Node(item, None)
        self._n += 1
        #raise NotImplementedError

    def dequeue(self) -> T:
        if self._n == 0:
            raise IndexError
        value = self._head._element
        self._head = self._head._next
        self._n -= 1
        return value
        #raise NotImplementedError

    def front(self) -> T:
        if self._n == 0:
            raise IndexError
        return self._head._element
        #raise NotImplementedError

    def __len__(self) -> int:
        return self._n
        #raise NotImplementedError
 