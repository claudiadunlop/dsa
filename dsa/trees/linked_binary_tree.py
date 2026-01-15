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
            raise NotImplementedError

        def __eq__(self, other: object) -> bool:
            """Return True if other represents the same position."""
            raise NotImplementedError

    def _validate(self, p: Tree.Position) -> _Node:
        """Return associated node if position is valid."""
        raise NotImplementedError

    def _make_position(self, node: Optional[_Node]) -> Optional[Position]:
        """Return Position instance for given node (or None if no node)."""
        raise NotImplementedError

    def __init__(self):
        """Create an empty binary tree."""
        raise NotImplementedError

    def __len__(self) -> int:
        raise NotImplementedError

    def root(self) -> Optional[Position]:
        raise NotImplementedError

    def parent(self, p: Tree.Position) -> Optional[Position]:
        raise NotImplementedError

    def left(self, p: Tree.Position) -> Optional[Position]:
        raise NotImplementedError

    def right(self, p: Tree.Position) -> Optional[Position]:
        raise NotImplementedError

    def add_root(self, e: T) -> Position:
        """Place element e at the root of an empty tree and return new Position.

        Raises:
            ValueError: If tree is not empty.
        """
        raise NotImplementedError

    def add_left(self, p: Tree.Position, e: T) -> Position:
        """Create a new left child for position p, storing element e.

        Returns:
            The Position of the new node.

        Raises:
            ValueError: If position p is invalid or already has a left child.
        """
        raise NotImplementedError

    def add_right(self, p: Tree.Position, e: T) -> Position:
        """Create a new right child for position p, storing element e.

        Returns:
            The Position of the new node.

        Raises:
            ValueError: If position p is invalid or already has a right child.
        """
        raise NotImplementedError

    def replace(self, p: Tree.Position, e: T) -> T:
        """Replace the element at position p with e and return old element.

        Args:
            p: A position in this tree.
            e: The new element to store.

        Returns:
            The element that was replaced.
        """
        raise NotImplementedError

    def delete(self, p: Tree.Position) -> T:
        """Delete the node at position p and replace it with its child, if any.

        Returns:
            The element that was stored at position p.

        Raises:
            ValueError: If position p is invalid or has two children.
        """
        raise NotImplementedError

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
        raise NotImplementedError
