"""Abstract base class defining the priority queue interface."""

from abc import ABC, abstractmethod
from typing import TypeVar, Generic, Tuple, Optional

K = TypeVar('K')
V = TypeVar('V')


class PriorityQueue(ABC, Generic[K, V]):
    """A collection that supports adding elements and removing the minimum.

    A priority queue stores key-value pairs and allows efficient access
    to the entry with the minimum key. Keys must be comparable.

    Core operations and their expected time complexities (for heap-based):
        add(key, value)     - Add a new entry              O(log n)
        min()               - Return (key, value) of min   O(1)
        remove_min()        - Remove and return minimum    O(log n)
        is_empty()          - Check if empty               O(1)
        __len__()           - Return number of entries     O(1)
    """

    @abstractmethod
    def add(self, key: K, value: V) -> None:
        """Add a key-value pair to the priority queue.

        Args:
            key: The priority key (smaller = higher priority).
            value: The value associated with this key.
        """
        pass

    @abstractmethod
    def min(self) -> Tuple[K, V]:
        """Return (but do not remove) the entry with minimum key.

        Returns:
            A tuple (key, value) for the minimum entry.

        Raises:
            IndexError: If the priority queue is empty.
        """
        pass

    @abstractmethod
    def remove_min(self) -> Tuple[K, V]:
        """Remove and return the entry with minimum key.

        Returns:
            A tuple (key, value) for the removed minimum entry.

        Raises:
            IndexError: If the priority queue is empty.
        """
        pass

    @abstractmethod
    def __len__(self) -> int:
        """Return the number of entries in the priority queue."""
        pass

    def is_empty(self) -> bool:
        """Return True if the priority queue contains no entries."""
        return len(self) == 0
