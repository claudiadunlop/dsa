"""Red-black tree implementation of a map."""

from dsa.maps.base import Map
from typing import TypeVar, Iterator, Optional

K = TypeVar('K')
V = TypeVar('V')


class RBTreeMap(Map[K, V]):
    """Map implementation using a red-black tree.

    A left-leaning red-black tree is a self-balancing binary search tree where each
    node has a color (red or black) and the tree maintains the following
    properties:
        1. Every node is either red or black
        2. The root is black
        3. All red links lean left
        4. We cannot have two red links in a row
        5. A node may not have two red links as children
        5. All paths from a node to descendant leaves contain the same
           number of black nodes

    These properties ensure O(log n) time for search, insert, and delete.
    """

    RED = True
    BLACK = False

    class _Node:
        """A node in the red-black tree."""
        __slots__ = '_key', '_value', '_left', '_right', '_parent', '_color'

        def __init__(self, key: K, value: V, color: bool = True,
                     parent: Optional['RBTreeMap._Node'] = None):
            self._key = key
            self._value = value
            self._color = color  # True = RED, False = BLACK
            self._left: Optional['RBTreeMap._Node'] = None
            self._right: Optional['RBTreeMap._Node'] = None
            self._parent = parent

    def __init__(self):
        """Create an empty red-black tree map."""
        self._root = None
        self._n = 0
        #raise NotImplementedError

    def __len__(self) -> int:
        return self._n
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
        
        return self._fix_insert(node)

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
        #raise NotImplementedError

    def _iter_help(self, node):
        if node._left is not None:
            yield from self._iter_help(node._left)
        yield node._key
        if node._right is not None:
            yield from self._iter_help(node._right)

    def _is_red(self, node: Optional[_Node]) -> bool:
        """Return True if node is red (None nodes are considered black)."""
        if node is None:
            return False
        return node._color
        #raise NotImplementedError

    def _rotate_left(self, node: _Node) -> None:
        """Perform a left rotation around the given node."""
        x = node._right
        node._right = x._left
        if x._left is not None:
            x._left._parent = None
        x._left = node
        x._parent = node._parent
        node._parent = x
        x._color = node._color
        node._color = True
        return x
    
        #raise NotImplementedError

    def _rotate_right(self, node: _Node) -> None:
        """Perform a right rotation around the given node."""
        x = node._left
        node._left = x._right
        if x._right is not None:
            x._right._parent = None
        x._right = node
        x._parent = node._parent
        node._parent = x
        x._color = node._color
        node._color = True
        return x
    
        #raise NotImplementedError

    def _flip_colors(self, node: _Node):
        node._color = not node._color
        node._left._color = not node._left._color
        node._right._color = not node._right._color


    def _fix_insert(self, node: _Node) -> None:
        """Restore red-black properties after insertion."""
        if self._is_red(node._right) == True and not self._is_red(node._left) == True:
            self._rotate_left(node)
        if self._is_red(node._left) == True and self._is_red(node._left._left) == True:
            self._rotate_right(node)
        if self._is_red(node._right) == True and self._is_red(node._left) == True:
            self._flip_colors(node)

        return node
        #raise NotImplementedError

    def __delitem__(self):
        return None