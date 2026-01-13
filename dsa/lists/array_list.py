"""Array-based list implementation."""

from dsa.lists.base import Sequence
from typing import TypeVar, Iterator

T = TypeVar('T')


class ArrayList(Sequence[T]):
    """Sequence implementation using a dynamic array.

    Uses a Python list as the underlying storage. Provides O(1) random
    access and O(1) amortized append, but O(n) insertion and deletion
    at arbitrary positions.
    """

    def __init__(self):
        """Create an empty array list."""
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
