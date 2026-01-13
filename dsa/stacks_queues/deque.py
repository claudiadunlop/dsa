"""Array-based deque implementation."""

from dsa.stacks_queues.base import Deque
from typing import TypeVar

T = TypeVar('T')


class ArrayDeque(Deque[T]):
    """Deque implementation using a circular array.

    Uses a fixed-size array with front and back indices that wrap around.
    The array is resized when capacity is reached.
    """

    DEFAULT_CAPACITY = 10

    def __init__(self):
        """Create an empty deque."""
        raise NotImplementedError

    def add_first(self, item: T) -> None:
        raise NotImplementedError

    def add_last(self, item: T) -> None:
        raise NotImplementedError

    def remove_first(self) -> T:
        raise NotImplementedError

    def remove_last(self) -> T:
        raise NotImplementedError

    def first(self) -> T:
        raise NotImplementedError

    def last(self) -> T:
        raise NotImplementedError

    def __len__(self) -> int:
        raise NotImplementedError
