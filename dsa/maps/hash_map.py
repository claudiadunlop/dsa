"""Hash table implementation of a map."""

from dsa.maps.base import Map
from typing import TypeVar, Iterator, Optional, List

K = TypeVar('K')
V = TypeVar('V')


class HashMap(Map[K, V]):
    """Map implementation using a hash table with separate chaining.

    Uses an array of buckets where each bucket holds entries that hash
    to the same index. Collisions are resolved by chaining entries in
    a list within each bucket.

    Load factor is maintained below a threshold by resizing the table
    when necessary.
    """

    DEFAULT_CAPACITY = 11
    LOAD_FACTOR_THRESHOLD = 0.75

    class item:
        def __init__(self, key, value):
            self._key = key
            self._value = value


    def __init__(self, capacity: int = DEFAULT_CAPACITY):
        """Create an empty hash map.

        Args:
            capacity: Initial number of buckets. Defaults to 11.
        """
        self._n = 0
        self._table = [[] for _ in range(capacity)]
        self._capacity = capacity
        #raise NotImplementedError

    def __len__(self) -> int:
        return self._n
        #raise NotImplementedError

    def __getitem__(self, key: K) -> V:
        index = self._hash(key)
        for i in self._table[index]:
            if i._key == key:
                return i._value
        raise KeyError
        #raise NotImplementedError

    def __setitem__(self, key: K, value: V) -> None:
        index = self._hash(key)
        item = self.item(key, value)
        for i in self._table[index]:
            if i._key == item._key:
                i._value = item._value
                return
        self._table[index].append(item)
        self._n += 1
        #raise NotImplementedError

    def __delitem__(self, key: K) -> None:
        index = self._hash(key)
        for i in self._table[index]:
            if i._key == key:
                i._key = None
                self._n -= 1
                return
        raise KeyError
        #raise NotImplementedError

    def __contains__(self, key: K) -> bool:
        index = self._hash(key)
        for i in self._table[index]:
            if i._key == key:
                return True
        return False
        #raise NotImplementedError

    def __iter__(self) -> Iterator[K]:
        for i in self._table:
            for j in i:
                yield j._key

        #raise NotImplementedError

    def _hash(self, key: K) -> int:
        """Compute the bucket index for the given key."""
        return hash(key) % self._capacity
        #raise NotImplementedError

    def _resize(self, new_capacity: int) -> None:
        """Resize the hash table to the given capacity."""
        if self._n < new_capacity:
            raise IndexError
        new_table = [[] for _ in range(new_capacity)]
        for i in range(self._table):
            new_table[i] = self._table[i]
        self._table = new_table
        self._capacity = new_capacity
        #raise NotImplementedError
