"""Linked list-based stack implementation."""

from dsa.stacks_queues.base import Stack
from typing import TypeVar, Optional

T = TypeVar('T')


class LinkedStack(Stack[T]):
    """Stack implementation using a singly linked list.

    The top of the stack is maintained at the head of the linked list,
    providing O(1) push and pop operations.
    """

    class _Node:
        """A node in the singly linked list."""
        __slots__ = '_element', '_next'

        def __init__(self, element: T, next: Optional['LinkedStack._Node'] = None):
            self._element = element
            self._next = next

    def __init__(self):
        """Create an empty stack."""
        raise NotImplementedError

    def push(self, item: T) -> None:
        raise NotImplementedError

    def pop(self) -> T:
        raise NotImplementedError

    def top(self) -> T:
        raise NotImplementedError

    def __len__(self) -> int:
        raise NotImplementedError
