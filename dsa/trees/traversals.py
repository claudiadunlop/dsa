"""Tree traversal algorithms."""

from dsa.trees.base import Tree, BinaryTree
from typing import TypeVar, Iterator, List, Callable, Optional
from dsa.stacks_queues.base import Queue

T = TypeVar('T')


def preorder(tree: Tree[T]) -> Iterator[T]:
    """Generate elements in preorder (root before children).

    In preorder traversal, we visit the root first, then recursively
    visit each subtree.

    Args:
        tree: The tree to traverse.

    Yields:
        Elements in preorder.
    """
    raise NotImplementedError


def postorder(tree: Tree[T]) -> Iterator[T]:
    """Generate elements in postorder (children before root).

    In postorder traversal, we recursively visit each subtree first,
    then visit the root.

    Args:
        tree: The tree to traverse.

    Yields:
        Elements in postorder.
    """
    raise NotImplementedError


def inorder(tree: BinaryTree[T]) -> Iterator[T]:
    """Generate elements in inorder (left, root, right).

    In inorder traversal of a binary tree, we visit the left subtree,
    then the root, then the right subtree.

    Args:
        tree: The binary tree to traverse.

    Yields:
        Elements in inorder.
    """
    raise NotImplementedError


def levelorder(tree: Tree[T]) -> Iterator[T]:
    """Generate elements in level order (breadth-first).

    In level order traversal, we visit all nodes at depth 0 (root),
    then all nodes at depth 1, then depth 2, etc.

    Args:
        tree: The tree to traverse.

    Yields:
        Elements in level order.
    """
    raise NotImplementedError
