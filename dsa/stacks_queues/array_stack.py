"""Array-based stack implementation."""

from dsa.stacks_queues.base import Stack
from typing import TypeVar

T = TypeVar('T')


class ArrayStack(Stack[T]):
    """Stack implementation using a Python list as underlying storage."""

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
