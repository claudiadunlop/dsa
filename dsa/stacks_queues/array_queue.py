"""Array-based queue implementation."""

from dsa.stacks_queues.base import Queue
from typing import TypeVar
import ctypes

T = TypeVar('T')


class ArrayQueue(Queue[T]):
    """Queue implementation using a circular array.

    Uses a fixed-size array with front and back indices that wrap around.
    The array is resized when capacity is reached.
    """

    DEFAULT_CAPACITY = 10

    def __init__(self):
        """Create an empty queue."""
        raise NotImplementedError

    def enqueue(self, item: T) -> None:
        raise NotImplementedError

    def dequeue(self) -> T:
        raise NotImplementedError

    def front(self) -> T:
        raise NotImplementedError

    def __len__(self) -> int:
        raise NotImplementedError

    def _make_array(self,c):
        return (c * ctypes.py_object) ()    
