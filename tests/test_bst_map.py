"""Tests for BSTMap implementation."""

import pytest
from dsa.maps.bst_map import BSTMap


class TestBSTMap:
    """Tests for the BSTMap class."""

    def test_new_map_is_empty(self):
        m = BSTMap()
        assert m.is_empty()
        assert len(m) == 0

    def test_setitem_getitem(self):
        m = BSTMap()
        m[5] = "five"
        assert m[5] == "five"

    def test_setitem_updates_existing(self):
        m = BSTMap()
        m[5] = "five"
        m[5] = "FIVE"
        assert m[5] == "FIVE"
        assert len(m) == 1

    def test_getitem_missing_raises(self):
        m = BSTMap()
        with pytest.raises(KeyError):
            _ = m[5]

    def test_delitem(self):
        m = BSTMap()
        m[5] = "five"
        del m[5]
        assert 5 not in m
        assert len(m) == 0

    def test_delitem_missing_raises(self):
        m = BSTMap()
        with pytest.raises(KeyError):
            del m[5]

    def test_contains(self):
        m = BSTMap()
        m[5] = "five"
        assert 5 in m
        assert 10 not in m

    def test_len(self):
        m = BSTMap()
        assert len(m) == 0
        m[5] = "five"
        assert len(m) == 1
        m[3] = "three"
        assert len(m) == 2
        del m[5]
        assert len(m) == 1

    def test_get_with_default(self):
        m = BSTMap()
        m[5] = "five"
        assert m.get(5) == "five"
        assert m.get(10) is None
        assert m.get(10, "default") == "default"

    def test_iteration_sorted_order(self):
        m = BSTMap()
        m[5] = "five"
        m[3] = "three"
        m[7] = "seven"
        m[1] = "one"
        m[9] = "nine"
        keys = list(m)
        assert keys == [1, 3, 5, 7, 9]

    def test_delete_leaf(self):
        m = BSTMap()
        m[5] = "five"
        m[3] = "three"
        m[7] = "seven"
        del m[3]
        assert list(m) == [5, 7]

    def test_delete_node_with_one_child(self):
        m = BSTMap()
        m[5] = "five"
        m[3] = "three"
        m[1] = "one"
        del m[3]
        assert list(m) == [1, 5]

    def test_delete_node_with_two_children(self):
        m = BSTMap()
        m[5] = "five"
        m[3] = "three"
        m[7] = "seven"
        m[2] = "two"
        m[4] = "four"
        del m[3]
        assert 3 not in m
        assert list(m) == [2, 4, 5, 7]

    def test_delete_root(self):
        m = BSTMap()
        m[5] = "five"
        m[3] = "three"
        m[7] = "seven"
        del m[5]
        assert 5 not in m
        assert len(m) == 2

    def test_many_items(self):
        m = BSTMap()
        import random
        values = list(range(100))
        random.shuffle(values)
        for v in values:
            m[v] = str(v)
        assert len(m) == 100
        assert list(m) == list(range(100))
