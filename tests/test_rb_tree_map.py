"""Tests for RBTreeMap implementation."""

import pytest
from dsa.maps.rb_tree_map import RBTreeMap


class TestRBTreeMap:
    """Tests for the RBTreeMap class."""

    def test_new_map_is_empty(self):
        m = RBTreeMap()
        assert m.is_empty()
        assert len(m) == 0

    def test_setitem_getitem(self):
        m = RBTreeMap()
        m[5] = "five"
        assert m[5] == "five"

    def test_setitem_updates_existing(self):
        m = RBTreeMap()
        m[5] = "five"
        m[5] = "FIVE"
        assert m[5] == "FIVE"
        assert len(m) == 1

    def test_getitem_missing_raises(self):
        m = RBTreeMap()
        with pytest.raises(KeyError):
            _ = m[5]

    def test_contains(self):
        m = RBTreeMap()
        m[5] = "five"
        assert 5 in m
        assert 10 not in m

    def test_iteration_sorted_order(self):
        m = RBTreeMap()
        m[5] = "five"
        m[3] = "three"
        m[7] = "seven"
        m[1] = "one"
        m[9] = "nine"
        keys = list(m)
        assert keys == [1, 3, 5, 7, 9]

    def test_sorted_insertion(self):
        """Red-black tree should handle sorted insertion efficiently."""
        m = RBTreeMap()
        for i in range(100):
            m[i] = str(i)
        assert len(m) == 100
        assert list(m) == list(range(100))

    def test_reverse_sorted_insertion(self):
        """Red-black tree should handle reverse-sorted insertion efficiently."""
        m = RBTreeMap()
        for i in range(99, -1, -1):
            m[i] = str(i)
        assert len(m) == 100
        assert list(m) == list(range(100))

    def test_keys_values_items(self):
        m = RBTreeMap()
        m[3] = "three"
        m[1] = "one"
        m[2] = "two"
        assert list(m.keys()) == [1, 2, 3]
        assert list(m.values()) == ["one", "two", "three"]
        assert list(m.items()) == [(1, "one"), (2, "two"), (3, "three")]
