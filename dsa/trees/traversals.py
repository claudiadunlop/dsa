"""Tree traversal algorithms."""

from dsa.trees.base import Tree, BinaryTree
from typing import TypeVar, Iterator, List, Callable, Optional
from dsa.stacks_queues.array_queue import ArrayQueue

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
    def _subtree_preorder(p):
        yield p.element()
        for c in tree.children(p):
            yield from _subtree_preorder(c)

    if not tree.is_empty():
        yield from _subtree_preorder(tree.root())
    #raise NotImplementedError


def postorder(tree: Tree[T]) -> Iterator[T]:
    """Generate elements in postorder (children before root).

    In postorder traversal, we recursively visit each subtree first,
    then visit the root.

    Args:
        tree: The tree to traverse.

    Yields:
        Elements in postorder.
    """
    def _subtree_postorder(p):
        for c in tree.children(p):
            yield from _subtree_postorder(c)
        yield p.element()

    if not tree.is_empty():
        yield from _subtree_postorder(tree.root())
    #raise NotImplementedError


def inorder(tree: BinaryTree[T]) -> Iterator[T]:
    """Generate elements in inorder (left, root, right).

    In inorder traversal of a binary tree, we visit the left subtree,
    then the root, then the right subtree.

    Args:
        tree: The binary tree to traverse.

    Yields:
        Elements in inorder.
    """
    def _subtree_inorder(p):
        if tree.left(p) is not None:
            yield from _subtree_inorder(tree.left(p))

        yield p.element()

        if tree.right(p) is not None:
            yield from _subtree_inorder(tree.right(p))

    if not tree.is_empty():
        yield from _subtree_inorder(tree.root())
    #raise NotImplementedError


def levelorder(tree: Tree[T]) -> Iterator[T]:
    """Generate elements in level order (breadth-first).

    In level order traversal, we visit all nodes at depth 0 (root),
    then all nodes at depth 1, then depth 2, etc.

    Args:
        tree: The tree to traverse.

    Yields:
        Elements in level order.
    """
    if not tree.is_empty():
        fringe = ArrayQueue()
        fringe.enqueue(tree.root())

        while not fringe.is_empty():
            p = fringe.dequeue()
            yield p.element()

            for c in tree.children(p):
                fringe.enqueue(c)

    #raise NotImplementedError
