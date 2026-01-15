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
        raise NotImplementedError

    def append(self, value: T) -> None:

        raise NotImplementedError

    def __getitem__(self, index: int) -> T:
        raise NotImplementedError

    def __setitem__(self, index: int, value: T) -> None:
        raise NotImplementedError

    def __delitem__(self, index: int) -> None:
        raise NotImplementedError

    def insert(self, index: int, value: T) -> None:
        raise NotImplementedError

    def __len__(self) -> int:
        raise NotImplementedError

    def __iter__(self) -> Iterator[T]:
        raise NotImplementedError
