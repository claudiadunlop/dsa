"""Tests for tree traversal algorithms.

These tests demonstrate two ways to traverse a tree:
1. Using the tree's methods directly (yields Positions)
2. Using the convenience functions in traversals.py (yields elements)

The class method approach is preferred as it follows the book's design
and gives access to Position objects when needed.
"""

import pytest
from dsa.trees.linked_binary_tree import LinkedBinaryTree
from dsa.trees import traversals


def build_sample_tree():
    """Build a sample binary tree for testing.

            1
           / \\
          2   3
         / \\
        4   5

    Preorder:   1, 2, 4, 5, 3
    Inorder:    4, 2, 5, 1, 3
    Postorder:  4, 5, 2, 3, 1
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
        # Class method approach (yields positions)
        result = [p.element() for p in tree.preorder()]
        assert result == []

    def test_single_node(self):
        tree = LinkedBinaryTree()
        tree.add_root(1)
        result = [p.element() for p in tree.preorder()]
        assert result == [1]

    def test_sample_tree(self):
        tree = build_sample_tree()
        result = [p.element() for p in tree.preorder()]
        assert result == [1, 2, 4, 5, 3]

    def test_convenience_function(self):
        """Test the traversals.preorder() convenience function."""
        tree = build_sample_tree()
        result = list(traversals.preorder(tree))
        assert result == [1, 2, 4, 5, 3]


class TestPostorder:
    """Tests for postorder traversal."""

    def test_empty_tree(self):
        tree = LinkedBinaryTree()
        result = [p.element() for p in tree.postorder()]
        assert result == []

    def test_single_node(self):
        tree = LinkedBinaryTree()
        tree.add_root(1)
        result = [p.element() for p in tree.postorder()]
        assert result == [1]

    def test_sample_tree(self):
        tree = build_sample_tree()
        result = [p.element() for p in tree.postorder()]
        assert result == [4, 5, 2, 3, 1]

    def test_convenience_function(self):
        """Test the traversals.postorder() convenience function."""
        tree = build_sample_tree()
        result = list(traversals.postorder(tree))
        assert result == [4, 5, 2, 3, 1]


class TestInorder:
    """Tests for inorder traversal."""

    def test_empty_tree(self):
        tree = LinkedBinaryTree()
        result = [p.element() for p in tree.inorder()]
        assert result == []

    def test_single_node(self):
        tree = LinkedBinaryTree()
        tree.add_root(1)
        result = [p.element() for p in tree.inorder()]
        assert result == [1]

    def test_sample_tree(self):
        tree = build_sample_tree()
        result = [p.element() for p in tree.inorder()]
        assert result == [4, 2, 5, 1, 3]

    def test_convenience_function(self):
        """Test the traversals.inorder() convenience function."""
        tree = build_sample_tree()
        result = list(traversals.inorder(tree))
        assert result == [4, 2, 5, 1, 3]


class TestLevelorder:
    """Tests for level-order (breadth-first) traversal."""

    def test_empty_tree(self):
        tree = LinkedBinaryTree()
        result = [p.element() for p in tree.levelorder()]
        assert result == []

    def test_single_node(self):
        tree = LinkedBinaryTree()
        tree.add_root(1)
        result = [p.element() for p in tree.levelorder()]
        assert result == [1]

    def test_sample_tree(self):
        tree = build_sample_tree()
        result = [p.element() for p in tree.levelorder()]
        assert result == [1, 2, 3, 4, 5]

    def test_convenience_function(self):
        """Test the traversals.levelorder() convenience function."""
        tree = build_sample_tree()
        result = list(traversals.levelorder(tree))
        assert result == [1, 2, 3, 4, 5]
