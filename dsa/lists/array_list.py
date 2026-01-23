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
        self._n = 0 #length
        self._capacity = 1 #total capacity of the array
        self._A = self._make_array(self._capacity) #array
            

    def __getitem__(self, index: int) -> T:
        if not 0 <= index < self._n:
            raise IndexError
        return self._A[index]
        #raise NotImplementedError

    def __setitem__(self, index: int, value: T) -> None:
        if not 0 <= index < self._n:
            raise IndexError
        self._A[index] = value
        #raise NotImplementedError

    def __delitem__(self, index: int) -> None:
        if not 0 <= index < self._n:
            raise IndexError
        for i in range(index, self._n-1):
            self._A[i] = self._A[i+1]
        self._A[self._n-1] = None
        self._n-=1
        #raise NotImplementedError

    def insert(self, index: int, value: T) -> None:
        if not 0 <= index <= self._n:
            raise IndexError
        if self._n >= self._capacity:
            self._capacity *= 2
            B = self._make_array(self._capacity)
            for i in range(self._n):
                B[i] = self._A[i]
            self._A = B
        for i in range(self._n, index, -1):
            self._A[i]=self._A[i-1]
        self._A[index]=value
        self._n += 1
            
        #raise NotImplementedError

    def __len__(self) -> int:
        return self._n
        #raise NotImplementedError

    def __iter__(self) -> Iterator[T]:
        for i in range(self._n):
            yield self._A[i]
        #raise NotImplementedError

    def _make_array(self,c):
        
        return (c * ctypes.py_object) ()
