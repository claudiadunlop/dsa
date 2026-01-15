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

    def __init__(self, capacity: int = DEFAULT_CAPACITY):
        """Create an empty hash map.

        Args:
            capacity: Initial number of buckets. Defaults to 11.
        """
        raise NotImplementedError

    def __len__(self) -> int:
        raise NotImplementedError

    def __getitem__(self, key: K) -> V:
        raise NotImplementedError

    def __setitem__(self, key: K, value: V) -> None:
        raise NotImplementedError

    def __delitem__(self, key: K) -> None:
        raise NotImplementedError

    def __contains__(self, key: K) -> bool:
        raise NotImplementedError

    def __iter__(self) -> Iterator[K]:
        raise NotImplementedError

    def _hash(self, key: K) -> int:
        """Compute the bucket index for the given key."""
        raise NotImplementedError

    def _resize(self, new_capacity: int) -> None:
        """Resize the hash table to the given capacity."""
        raise NotImplementedError
