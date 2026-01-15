"""Tests for tree traversal algorithms."""

import pytest
from dsa.trees.linked_binary_tree import LinkedBinaryTree
from dsa.trees.traversals import preorder, postorder, inorder, levelorder


def build_sample_tree():
    """Build a sample binary tree for testing.

            1
           / \\
          2   3
         / \\
        4   5

    Preorder:  1, 2, 4, 5, 3
    Inorder:   4, 2, 5, 1, 3
    Postorder: 4, 5, 2, 3, 1
    Levelorder: 1, 2, 3, 4, 5
    """
    tree = LinkedBinaryTree()
    root = tree.add_root(1)
    left = tree.add_left(root, 2)
    tree.add_right(root, 3)
    tree.add_left(left, 4)
    tree.add_right(left, 5)
    return tree


class TestPreorder:
    """Tests for preorder traversal."""

    def test_empty_tree(self):
        tree = LinkedBinaryTree()
        result = list(preorder(tree))
        assert result == []

    def test_single_node(self):
        tree = LinkedBinaryTree()
        tree.add_root(1)
        result = list(preorder(tree))
        assert result == [1]

    def test_sample_tree(self):
        tree = build_sample_tree()
        result = list(preorder(tree))
        assert result == [1, 2, 4, 5, 3]


class TestPostorder:
    """Tests for postorder traversal."""

    def test_empty_tree(self):
        tree = LinkedBinaryTree()
        result = list(postorder(tree))
        assert result == []

    def test_single_node(self):
        tree = LinkedBinaryTree()
        tree.add_root(1)
        result = list(postorder(tree))
        assert result == [1]

    def test_sample_tree(self):
        tree = build_sample_tree()
        result = list(postorder(tree))
        assert result == [4, 5, 2, 3, 1]


class TestInorder:
    """Tests for inorder traversal."""

    def test_empty_tree(self):
        tree = LinkedBinaryTree()
        result = list(inorder(tree))
        assert result == []

    def test_single_node(self):
        tree = LinkedBinaryTree()
        tree.add_root(1)
        result = list(inorder(tree))
        assert result == [1]

    def test_sample_tree(self):
        tree = build_sample_tree()
        result = list(inorder(tree))
        assert result == [4, 2, 5, 1, 3]


class TestLevelorder:
    """Tests for level-order (breadth-first) traversal."""

    def test_empty_tree(self):
        tree = LinkedBinaryTree()
        result = list(levelorder(tree))
        assert result == []

    def test_single_node(self):
        tree = LinkedBinaryTree()
        tree.add_root(1)
        result = list(levelorder(tree))
        assert result == [1]

    def test_sample_tree(self):
        tree = build_sample_tree()
        result = list(levelorder(tree))
        assert result == [1, 2, 3, 4, 5]
