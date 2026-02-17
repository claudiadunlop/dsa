"""Linked structure implementation of a binary tree."""

from dsa.trees.base import BinaryTree, Tree
from typing import TypeVar, Optional, Iterator

T = TypeVar('T')


class LinkedBinaryTree(BinaryTree[T]):
    """Binary tree implementation using a linked structure.

    Each node contains an element and references to parent, left child,
    and right child nodes.
    """

    class _Node:
        """Lightweight node class for storing tree elements."""
        __slots__ = '_element', '_parent', '_left', '_right'

        def __init__(self, element: T,
                     parent: Optional['LinkedBinaryTree._Node'] = None,
                     left: Optional['LinkedBinaryTree._Node'] = None,
                     right: Optional['LinkedBinaryTree._Node'] = None):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right

    class Position(Tree.Position):
        """An abstraction representing the location of a single element."""

        def __init__(self, container: 'LinkedBinaryTree', node: 'LinkedBinaryTree._Node'):
            """Constructor should not be invoked by user."""
            self._container = container
            self._node = node

        def element(self) -> T:
            """Return the element stored at this position."""
            return self._node._element
            #raise NotImplementedError

        def __eq__(self, other: object) -> bool:
            """Return True if other represents the same position."""
            return type(other) is type(self) and other._node is self._node
            #raise NotImplementedError

    def _validate(self, p: Tree.Position) -> _Node:
        """Return associated node if position is valid."""
        if not isinstance(p, self.Position):
            raise TypeError
        if p._container is not self:
            raise ValueError
        if p._node._parent is p._node:
            raise ValueError
        return p._node
        #raise NotImplementedError

    def _make_position(self, node: Optional[_Node]) -> Optional[Position]:
        """Return Position instance for given node (or None if no node)."""
        return self.Position(self, node) if node is not None else None
        #raise NotImplementedError

    def __init__(self):
        """Create an empty binary tree."""
        self._n = 0
        self._root = None
       #raise NotImplementedError

    def __len__(self) -> int:
        return self._n
        #raise NotImplementedError

    def root(self) -> Optional[Position]:
        return self._make_position(self._root)
        #raise NotImplementedError

    def parent(self, p: Tree.Position) -> Optional[Position]:
        node = self._validate(p)
        return self._make_position(node._parent)
        #raise NotImplementedError

    def left(self, p: Tree.Position) -> Optional[Position]:
        node = self._validate(p)
        return self._make_position(node._left)
        #raise NotImplementedError

    def right(self, p: Tree.Position) -> Optional[Position]:
        node = self._validate(p)
        return self._make_position(node._right)
        #raise NotImplementedError

    def add_root(self, e: T) -> Position:
        """Place element e at the root of an empty tree and return new Position.

        Raises:
            ValueError: If tree is not empty.
        """
        if self._root is not None:
            raise ValueError('Root exists')
        self._n = 1
        self._root = self._Node(e)
        return self._make_position(self._root)
        #raise NotImplementedError

    def add_left(self, p: Tree.Position, e: T) -> Position:
        """Create a new left child for position p, storing element e.

        Returns:
            The Position of the new node.

        Raises:
            ValueError: If position p is invalid or already has a left child.
        """
        node = self._validate(p)
        if node._left is not None:
            raise ValueError('Root exists')
        self._n += 1
        node._left = self._Node(e, node)
        return self._make_position(node._left)
        #raise NotImplementedError

    def add_right(self, p: Tree.Position, e: T) -> Position:
        """Create a new right child for position p, storing element e.

        Returns:
            The Position of the new node.

        Raises:
            ValueError: If position p is invalid or already has a right child.
        """
        node = self._validate(p)
        if node._right is not None:
            raise ValueError('Right child exists')
        self._n += 1
        node._right = self._Node(e, node)
        return self._make_position(node._right)
        #raise NotImplementedError

    def replace(self, p: Tree.Position, e: T) -> T:
        """Replace the element at position p with e and return old element.

        Args:
            p: A position in this tree.
            e: The new element to store.

        Returns:
            The element that was replaced.
        """
        node = self._validate(p)
        old = node._element
        node._element = e
        return old
        #raise NotImplementedError

    def delete(self, p: Tree.Position) -> T:
        """Delete the node at position p and replace it with its child, if any.

        Returns:
            The element that was stored at position p.

        Raises:
            ValueError: If position p is invalid or has two children.
        """
        node = self._validate(p)
        if self.num_children(p) == 2:
            raise ValueError('Position has two children')
        child = node._left if node._left else node._right
        if child is not None:
            child._parent = node._parent
        if node is self._root:
            self._root = child
        else:
            parent = node._parent
            if node is parent._left:
                parent._left = child
            else:
                parent._right = child
        self._n -= 1
        node._parent = node
        return node._element
        #raise NotImplementedError

    def attach(self, p: Tree.Position, t1: 'LinkedBinaryTree', t2: 'LinkedBinaryTree') -> None:
        """Attach trees t1 and t2 as left and right subtrees of leaf p.

        Args:
            p: A leaf position in this tree.
            t1: A LinkedBinaryTree to attach as left subtree.
            t2: A LinkedBinaryTree to attach as right subtree.

        Raises:
            ValueError: If p is not a leaf.
            TypeError: If t1 or t2 is not a LinkedBinaryTree.
        """
        node = self._validate(p)
        if not self.is_leaf(p):
            raise ValueError('Position must be a leaf')
        if not type(self) is type(t1) is type(t2):
            raise TypeError('Tree types must match')
        self._n += len(t1) + len(t2)
        if not t1.is_empty():
            t1._root._parent = node
            node._left = t1._root
            t1._root = None
            t1._n = 0
        if not t2.is_empty():
            t2._root._parent = node
            node._right = t2._root
            t2._root = None
            t2._n = 0
        #raise NotImplementedError
