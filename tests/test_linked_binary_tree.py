"""Tests for LinkedBinaryTree implementation."""

import pytest
from dsa.trees.linked_binary_tree import LinkedBinaryTree


class TestLinkedBinaryTree:
    """Tests for the LinkedBinaryTree class."""

    def test_new_tree_is_empty(self):
        tree = LinkedBinaryTree()
        assert tree.is_empty()
        assert len(tree) == 0

    def test_add_root(self):
        tree = LinkedBinaryTree()
        root = tree.add_root(1)
        assert not tree.is_empty()
        assert len(tree) == 1
        assert root.element() == 1
        assert tree.root() == root

    def test_add_root_nonempty_raises(self):
        tree = LinkedBinaryTree()
        tree.add_root(1)
        with pytest.raises(ValueError):
            tree.add_root(2)

    def test_add_left(self):
        tree = LinkedBinaryTree()
        root = tree.add_root(1)
        left = tree.add_left(root, 2)
        assert len(tree) == 2
        assert left.element() == 2
        assert tree.left(root) == left
        assert tree.parent(left) == root

    def test_add_right(self):
        tree = LinkedBinaryTree()
        root = tree.add_root(1)
        right = tree.add_right(root, 3)
        assert len(tree) == 2
        assert right.element() == 3
        assert tree.right(root) == right
        assert tree.parent(right) == root

    def test_add_left_already_exists_raises(self):
        tree = LinkedBinaryTree()
        root = tree.add_root(1)
        tree.add_left(root, 2)
        with pytest.raises(ValueError):
            tree.add_left(root, 3)

    def test_add_right_already_exists_raises(self):
        tree = LinkedBinaryTree()
        root = tree.add_root(1)
        tree.add_right(root, 2)
        with pytest.raises(ValueError):
            tree.add_right(root, 3)

    def test_is_root(self):
        tree = LinkedBinaryTree()
        root = tree.add_root(1)
        left = tree.add_left(root, 2)
        assert tree.is_root(root)
        assert not tree.is_root(left)

    def test_is_leaf(self):
        tree = LinkedBinaryTree()
        root = tree.add_root(1)
        left = tree.add_left(root, 2)
        assert tree.is_leaf(left)
        assert not tree.is_leaf(root)

    def test_sibling(self):
        tree = LinkedBinaryTree()
        root = tree.add_root(1)
        left = tree.add_left(root, 2)
        right = tree.add_right(root, 3)
        assert tree.sibling(left) == right
        assert tree.sibling(right) == left
        assert tree.sibling(root) is None

    def test_num_children(self):
        tree = LinkedBinaryTree()
        root = tree.add_root(1)
        assert tree.num_children(root) == 0
        tree.add_left(root, 2)
        assert tree.num_children(root) == 1
        tree.add_right(root, 3)
        assert tree.num_children(root) == 2

    def test_replace(self):
        tree = LinkedBinaryTree()
        root = tree.add_root(1)
        old = tree.replace(root, 10)
        assert old == 1
        assert root.element() == 10

    def test_delete_leaf(self):
        tree = LinkedBinaryTree()
        root = tree.add_root(1)
        left = tree.add_left(root, 2)
        element = tree.delete(left)
        assert element == 2
        assert len(tree) == 1
        assert tree.left(root) is None

    def test_delete_with_one_child(self):
        tree = LinkedBinaryTree()
        root = tree.add_root(1)
        left = tree.add_left(root, 2)
        left_left = tree.add_left(left, 3)
        tree.delete(left)
        assert len(tree) == 2
        assert tree.left(root) == left_left
        assert tree.parent(left_left) == root

    def test_delete_with_two_children_raises(self):
        tree = LinkedBinaryTree()
        root = tree.add_root(1)
        left = tree.add_left(root, 2)
        tree.add_left(left, 3)
        tree.add_right(left, 4)
        with pytest.raises(ValueError):
            tree.delete(left)

    def test_depth(self):
        tree = LinkedBinaryTree()
        root = tree.add_root(1)
        left = tree.add_left(root, 2)
        left_left = tree.add_left(left, 3)
        assert tree.depth(root) == 0
        assert tree.depth(left) == 1
        assert tree.depth(left_left) == 2

    def test_height(self):
        tree = LinkedBinaryTree()
        root = tree.add_root(1)
        left = tree.add_left(root, 2)
        tree.add_left(left, 3)
        tree.add_right(root, 4)
        assert tree.height(root) == 2
        assert tree.height(left) == 1
