"""Abstract base class defining the map (associative array) interface."""

from abc import ABC, abstractmethod
from typing import TypeVar, Generic, Iterator, Tuple

K = TypeVar('K')
V = TypeVar('V')


class Map(ABC, Generic[K, V]):
    """A collection of key-value pairs with unique keys.

    A map (also called associative array, dictionary, or symbol table)
    associates keys with values. Each key appears at most once; inserting
    a duplicate key overwrites the previous value.

    Core operations and their expected time complexities vary by
    implementation:

                        Hash-based      Tree-based (balanced)
        __getitem__     O(1) avg        O(log n)
        __setitem__     O(1) avg        O(log n)
        __delitem__     O(1) avg        O(log n)
        __contains__    O(1) avg        O(log n)
        __len__         O(1)            O(1)
        __iter__        O(n)            O(n)

    This interface uses Python's bracket syntax for access:
        m[key] = value   calls __setitem__
        value = m[key]   calls __getitem__
        del m[key]       calls __delitem__
        key in m         calls __contains__
    """

    @abstractmethod
    def __getitem__(self, key: K) -> V:
        """Return the value associated with key.

        Args:
            key: The key to look up.

        Returns:
            The value associated with the key.

        Raises:
            KeyError: If the key is not found.
        """
        pass

    @abstractmethod
    def __setitem__(self, key: K, value: V) -> None:
        """Associate value with key, overwriting any existing value.

        Args:
            key: The key to insert or update.
            value: The value to associate with the key.
        """
        pass

    @abstractmethod
    def __delitem__(self, key: K) -> None:
        """Remove the key and its associated value.

        Args:
            key: The key to remove.

        Raises:
            KeyError: If the key is not found.
        """
        pass

    @abstractmethod
    def __contains__(self, key: K) -> bool:
        """Return True if the key is in the map.

        Args:
            key: The key to search for.
        """
        pass

    @abstractmethod
    def __len__(self) -> int:
        """Return the number of key-value pairs in the map."""
        pass

    @abstractmethod
    def __iter__(self) -> Iterator[K]:
        """Iterate over keys in the map.

        The iteration order depends on the implementation:
        - Hash-based: arbitrary order
        - Tree-based: sorted order by key (not strictly required)

        Yields:
            Each key in the map.
        """
        pass

    def is_empty(self) -> bool:
        """Return True if the map contains no key-value pairs."""
        return len(self) == 0

    def get(self, key: K, default: V = None) -> V:
        """Return the value for key if present, else default.

        Unlike __getitem__, this does not raise KeyError for missing keys.

        Args:
            key: The key to look up.
            default: Value to return if key is not found.

        Returns:
            The associated value, or default if key is absent.
        """
        try:
            return self[key]
        except KeyError:
            return default

    def keys(self) -> Iterator[K]:
        """Return an iterator over the map's keys.

        Equivalent to iter(self).
        """
        return iter(self)

    def values(self) -> Iterator[V]:
        """Return an iterator over the map's values."""
        for key in self:
            yield self[key]

    def items(self) -> Iterator[Tuple[K, V]]:
        """Return an iterator over (key, value) pairs."""
        for key in self:
            yield (key, self[key])
