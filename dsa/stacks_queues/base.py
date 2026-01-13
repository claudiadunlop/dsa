"""Abstract base classes defining the stack, queue, and deque interfaces."""

from abc import ABC, abstractmethod
from typing import TypeVar, Generic

T = TypeVar('T')


class Stack(ABC, Generic[T]):
    """A last-in, first-out (LIFO) collection.

    A stack supports insertion and removal only at one end, called the "top."
    The most recently added element is always the first to be removed.

    Core operations and their expected time complexities:
        push(item)  - Add item to top           O(1) amortized or worst-case
        pop()       - Remove and return top     O(1)
        top()       - Return top without removing   O(1)
        is_empty()  - Check if stack is empty   O(1)
        __len__()   - Return number of items    O(1)
    """

    @abstractmethod
    def push(self, item: T) -> None:
        """Add an item to the top of the stack.

        Args:
            item: The element to add.
        """
        pass

    @abstractmethod
    def pop(self) -> T:
        """Remove and return the item at the top of the stack.

        Returns:
            The most recently added item.

        Raises:
            IndexError: If the stack is empty.
        """
        pass

    @abstractmethod
    def top(self) -> T:
        """Return the item at the top without removing it.

        Returns:
            The most recently added item.

        Raises:
            IndexError: If the stack is empty.
        """
        pass

    def is_empty(self) -> bool:
        """Return True if the stack contains no items.

        This default implementation relies on __len__. Subclasses may
        override for efficiency if needed.
        """
        return len(self) == 0

    @abstractmethod
    def __len__(self) -> int:
        """Return the number of items in the stack."""
        pass


class Queue(ABC, Generic[T]):
    """A first-in, first-out (FIFO) collection.

    A queue supports insertion at the back (enqueue) and removal from
    the front (dequeue). The oldest element is always the first to be removed.

    Core operations and their expected time complexities:
        enqueue(item)   - Add item to back          O(1) amortized
        dequeue()       - Remove and return front   O(1) amortized
        front()         - Return front without removing O(1)
        is_empty()      - Check if queue is empty   O(1)
        __len__()       - Return number of items    O(1)
    """

    @abstractmethod
    def enqueue(self, item: T) -> None:
        """Add an item to the back of the queue.

        Args:
            item: The element to add.
        """
        pass

    @abstractmethod
    def dequeue(self) -> T:
        """Remove and return the item at the front of the queue.

        Returns:
            The oldest item in the queue.

        Raises:
            IndexError: If the queue is empty.
        """
        pass

    @abstractmethod
    def front(self) -> T:
        """Return the item at the front without removing it.

        Returns:
            The oldest item in the queue.

        Raises:
            IndexError: If the queue is empty.
        """
        pass

    def is_empty(self) -> bool:
        """Return True if the queue contains no items."""
        return len(self) == 0

    @abstractmethod
    def __len__(self) -> int:
        """Return the number of items in the queue."""
        pass


class Deque(ABC, Generic[T]):
    """A double-ended queue supporting insertion and removal at both ends.

    A deque (pronounced "deck") generalizes both stacks and queues by
    allowing efficient insertion and removal at either end.

    Core operations and their expected time complexities:
        add_first(item)     - Add item to front         O(1) amortized
        add_last(item)      - Add item to back          O(1) amortized
        remove_first()      - Remove and return front   O(1) amortized
        remove_last()       - Remove and return back    O(1) amortized
        first()             - Return front without removing O(1)
        last()              - Return back without removing  O(1)
        is_empty()          - Check if deque is empty   O(1)
        __len__()           - Return number of items    O(1)
    """

    @abstractmethod
    def add_first(self, item: T) -> None:
        """Add an item to the front of the deque.

        Args:
            item: The element to add.
        """
        pass

    @abstractmethod
    def add_last(self, item: T) -> None:
        """Add an item to the back of the deque.

        Args:
            item: The element to add.
        """
        pass

    @abstractmethod
    def remove_first(self) -> T:
        """Remove and return the item at the front of the deque.

        Returns:
            The item at the front.

        Raises:
            IndexError: If the deque is empty.
        """
        pass

    @abstractmethod
    def remove_last(self) -> T:
        """Remove and return the item at the back of the deque.

        Returns:
            The item at the back.

        Raises:
            IndexError: If the deque is empty.
        """
        pass

    @abstractmethod
    def first(self) -> T:
        """Return the item at the front without removing it.

        Returns:
            The item at the front.

        Raises:
            IndexError: If the deque is empty.
        """
        pass

    @abstractmethod
    def last(self) -> T:
        """Return the item at the back without removing it.

        Returns:
            The item at the back.

        Raises:
            IndexError: If the deque is empty.
        """
        pass

    def is_empty(self) -> bool:
        """Return True if the deque contains no items."""
        return len(self) == 0

    @abstractmethod
    def __len__(self) -> int:
        """Return the number of items in the deque."""
        pass
