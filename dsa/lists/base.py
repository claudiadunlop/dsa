"""Abstract base class defining the sequence (list) interface."""

from abc import ABC, abstractmethod
from typing import TypeVar, Generic, Iterator

T = TypeVar('T')


class Sequence(ABC, Generic[T]):
    """A mutable sequence of elements with index-based access.

    A sequence maintains elements in a linear order, accessible by
    non-negative integer indices. Supports insertion, deletion, and
    modification at any position.

    Core operations and their expected time complexities:

                            Array-based     Linked
        __getitem__(i)      O(1)            O(n)
        __setitem__(i, v)   O(1)            O(n)
        __delitem__(i)      O(n)            O(n)
        insert(i, v)        O(n)            O(n)
        append(v)           O(1) amortized  O(1) with tail pointer
        __len__()           O(1)            O(1)
        __iter__()          O(n)            O(n)

    Indices follow Python conventions:
        - Valid indices are 0 to len-1
        - IndexError raised for out-of-bounds access
    """

    @abstractmethod
    def __getitem__(self, index: int) -> T:
        """Return the element at the given index.

        Args:
            index: The position of the element to retrieve.

        Returns:
            The element at the specified position.

        Raises:
            IndexError: If index is out of bounds.
        """
        pass

    @abstractmethod
    def __setitem__(self, index: int, value: T) -> None:
        """Replace the element at the given index.

        Args:
            index: The position of the element to replace.
            value: The new value to store.

        Raises:
            IndexError: If index is out of bounds.
        """
        pass

    @abstractmethod
    def __delitem__(self, index: int) -> None:
        """Remove the element at the given index.

        Elements after the removed element shift down by one position.

        Args:
            index: The position of the element to remove.

        Raises:
            IndexError: If index is out of bounds.
        """
        pass

    @abstractmethod
    def insert(self, index: int, value: T) -> None:
        """Insert a value at the given index.

        Elements at and after the index shift up by one position.
        If index equals len(self), the value is appended.

        Args:
            index: The position at which to insert.
            value: The element to insert.

        Raises:
            IndexError: If index < 0 or index > len(self).
        """
        pass

    @abstractmethod
    def __len__(self) -> int:
        """Return the number of elements in the sequence."""
        pass

    @abstractmethod
    def __iter__(self) -> Iterator[T]:
        """Return an iterator over the elements in order."""
        pass

    def append(self, value: T) -> None:
        """Add an element to the end of the sequence.

        This default implementation calls insert at len(self).
        Subclasses may override for efficiency.

        Args:
            value: The element to append.
        """
        self.insert(len(self), value)

    def is_empty(self) -> bool:
        """Return True if the sequence contains no elements."""
        return len(self) == 0

    def __contains__(self, value: T) -> bool:
        """Return True if value is in the sequence.

        Uses linear search with equality comparison.
        """
        for item in self:
            if item == value:
                return True
        return False
