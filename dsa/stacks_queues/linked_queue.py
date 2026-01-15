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
        """Create an empty queue."""
        raise NotImplementedError

    def enqueue(self, item: T) -> None:
        raise NotImplementedError

    def dequeue(self) -> T:
        raise NotImplementedError

    def front(self) -> T:
        raise NotImplementedError

    def __len__(self) -> int:
        raise NotImplementedError
