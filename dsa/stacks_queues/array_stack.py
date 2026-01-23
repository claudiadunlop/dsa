"""Array-based stack implementation."""

from dsa.stacks_queues.base import Stack
from typing import TypeVar
import ctypes

T = TypeVar('T')


class ArrayStack(Stack[T]):
    """Stack implementation using a Python list as underlying storage."""

    def __init__(self):
        """Create an empty stack."""
        self._n = 0 #length
        self._capacity = 1 #total capacity of the array
        self._A = self._make_array(self._capacity) #array
        #raise NotImplementedError

    def push(self, item: T) -> None:
        if self._n >= self._capacity:
            self._capacity *= 2
            B = self._make_array(self._capacity)
            for i in range(self._n):
                B[i] = self._A[i]
            self._A = B
        self._A[self._n] = item
        self._n +=1
        #raise NotImplementedError

    def pop(self) -> T:
        if self._n == 0:
            raise IndexError
        top_value = self._A[self._n-1]
        self._A[self._n-1] = None
        self._n -= 1
        return top_value
        #raise NotImplementedError

    def top(self) -> T:
        if self._n == 0:
            raise IndexError
        return self._A[self._n-1]
        #raise NotImplementedError

    def __len__(self) -> int:
        return self._n
        #raise NotImplementedError

    def _make_array(self,c):
        return (c * ctypes.py_object) ()
