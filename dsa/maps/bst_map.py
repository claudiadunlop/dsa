"""Binary search tree implementation of a map."""

from dsa.maps.base import Map
from typing import TypeVar, Iterator, Optional

K = TypeVar('K')
V = TypeVar('V')


class BSTMap(Map[K, V]):
    """Map implementation using an unbalanced binary search tree.

    Each node contains a key-value pair. The BST property ensures that
    for each node, all keys in the left subtree are less than the node's
    key, and all keys in the right subtree are greater.

    Note: This unbalanced implementation has O(n) worst-case time complexity
    for all operations when the tree becomes degenerate (e.g., inserting
    sorted keys). See RBTreeMap for a balanced alternative.
    """

    class _Node:
        """A node in the binary search tree."""
        __slots__ = '_key', '_value', '_left', '_right', '_parent'

        def __init__(self, key: K, value: V,
                     parent: Optional['BSTMap._Node'] = None):
            self._key = key
            self._value = value
            self._left: Optional['BSTMap._Node'] = None
            self._right: Optional['BSTMap._Node'] = None
            self._parent = parent

    def __init__(self):
        """Create an empty BST map."""
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

    def _search(self, key: K, node: Optional[_Node]) -> Optional[_Node]:
        """Search for a node with the given key starting from node.

        Returns the node if found, or None if not found.
        """
        raise NotImplementedError

    def _subtree_min(self, node: _Node) -> _Node:
        """Return the node with minimum key in subtree rooted at node."""
        raise NotImplementedError

    def _subtree_max(self, node: _Node) -> _Node:
        """Return the node with maximum key in subtree rooted at node."""
        raise NotImplementedError
