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
        self._n = 0 #length
        self._capacity = 1 #total capacity of the array
        self._A = self._make_array(self._capacity) #array
        #raise NotImplementedError

    def enqueue(self, item: T) -> None:
        if self._n >= self._capacity:
            self._capacity *= 2
            B = self._make_array(self._capacity)
            for i in range(self._n):
                B[i] = self._A[i]
            self._A = B
        self._A[self._n]=item 
        self._n +=1
        #raise NotImplementedError

    def dequeue(self) -> T:
        if self._n == 0:
            raise IndexError
        first_value = self._A[0]
        for i in range(1, self._n):
            self._A[i-1] = self._A[i]
        self._A[self._n-1] = None
        self._n -= 1
        return first_value
        #raise NotImplementedError

    def front(self) -> T:
        if self._n == 0:
            raise IndexError
        return self._A[0]
        #raise NotImplementedError

    def __len__(self) -> int:
        return self._n
        #raise NotImplementedError

    def _make_array(self,c):
        return (c * ctypes.py_object) ()    
