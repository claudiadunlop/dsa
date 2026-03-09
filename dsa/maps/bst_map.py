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
        self._root = None
        self._n = 0
        #raise NotImplementedError

    def __len__(self) -> int:
        return self._n
        #raise NotImplementedError

    def __getitem__(self, key: K) -> V:
        node = self._search(key, self._root)
        if node is None:
            raise KeyError
        return node._value
        #raise NotImplementedError

    def __setitem__(self, key: K, value: V) -> None:
        if self._root == None:
            self._root = self._Node(key, value)
            self._n = 1
            return
        
        self.add_helper(self._root, key, value, self._root)
        #raise NotImplementedError
    
    def add_helper(self, node, key, value, parent):
        if node is None:
            node = self._Node(key, value, parent)
            self._n += 1
            return node
        if node._key == key:
            node._value = value
        if key < node._key:
            node._left = self.add_helper(node._left, key, value, node)
        if key > node._key:
            node._right = self.add_helper(node._right, key, value, node)
        return node
        
    def __delitem__(self, key: K) -> None:
        deleted_node = self._search(key, self._root)
        
        if deleted_node is None:
            raise KeyError
        if deleted_node._right == None:
            self._replace_node(deleted_node, deleted_node._left)
            self._n -= 1
        elif deleted_node._left == None:
            self._replace_node(deleted_node, deleted_node._right)
            self._n -= 1
        elif deleted_node._right and deleted_node._left:
            newnode = self._subtree_max(deleted_node._left)
            if newnode._parent != deleted_node:
                self._replace_node(newnode, newnode._left)
                newnode._left = deleted_node._left
                if newnode._left is not None:
                    newnode._left._parent = newnode
            self._replace_node(deleted_node, newnode)
            newnode._right = deleted_node._right
            if newnode._left is not None:
                newnode._left._parent = newnode
            self._n -= 1
        
        #raise NotImplementedError

    def _replace_node(self, node, child):
        parent = node._parent

        if parent is None:
            self._root = child
        elif parent._right == node:
            parent._right = child
        elif parent._left == node:
            parent._left = child
        
        if child is not None:
            child._parent = parent

    def __contains__(self, key: K) -> bool:
        node = self._search(key, self._root)
        if node is None:
            return False
        else:
            return True
        #raise NotImplementedError

    def __iter__(self) -> Iterator[K]:
        node = self._root
        if node is None:
            return
        yield from self._iter_help(node)
        
    def _iter_help(self, node):
        if node._left is not None:
            yield from self._iter_help(node._left)
        yield node._key
        if node._right is not None:
            yield from self._iter_help(node._right)
            
        #raise NotImplementedError

    def _search(self, key: K, node: Optional[_Node]) -> Optional[_Node]:
        """Search for a node with the given key starting from node.

        Returns the node if found, or None if not found.
        """
        while node is not None:
            if key == node._key:
                return node
            elif key < node._key:
                node = node._left
            else:
                node = node._right
        return None
    
        #raise NotImplementedError

    def _subtree_min(self, node: _Node) -> _Node:
        """Return the node with minimum key in subtree rooted at node."""
        while node._left is not None:
            node = node._left
        return node
        #raise NotImplementedError

    def _subtree_max(self, node: _Node) -> _Node:
        """Return the node with maximum key in subtree rooted at node."""
        while node._right is not None:
            node = node._right
        return node
        #raise NotImplementedError
