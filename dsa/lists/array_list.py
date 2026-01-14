"""Array-based list implementation."""

from dsa.lists.base import Sequence
from typing import TypeVar, Iterator
import ctypes

T = TypeVar('T')


class ArrayList(Sequence[T]):
    """Sequence implementation using a dynamic array.

    *Must* use ctypes array as the underlying storage! Provides O(1) random
    access and O(1) amortized append, but O(n) insertion and deletion
    at arbitrary positions.
    """

    def __init__(self):
        """Create an empty array list."""
        self._n = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)

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

    def _make_array(self,c):
        return (c * ctypes.py_object) ()
