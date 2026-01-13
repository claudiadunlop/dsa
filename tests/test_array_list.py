"""Tests for ArrayList implementation."""

import pytest
from dsa.lists.array_list import ArrayList


class TestArrayList:
    """Tests for the ArrayList class."""

    def test_new_list_is_empty(self):
        lst = ArrayList()
        assert lst.is_empty()
        assert len(lst) == 0

    def test_append_single_item(self):
        lst = ArrayList()
        lst.append(42)
        assert not lst.is_empty()
        assert len(lst) == 1
        assert lst[0] == 42

    def test_append_multiple_items(self):
        lst = ArrayList()
        lst.append(1)
        lst.append(2)
        lst.append(3)
        assert len(lst) == 3
        assert lst[0] == 1
        assert lst[1] == 2
        assert lst[2] == 3

    def test_getitem_negative_index_raises(self):
        lst = ArrayList()
        lst.append(1)
        with pytest.raises(IndexError):
            _ = lst[-1]

    def test_getitem_out_of_bounds_raises(self):
        lst = ArrayList()
        lst.append(1)
        with pytest.raises(IndexError):
            _ = lst[1]

    def test_setitem(self):
        lst = ArrayList()
        lst.append(1)
        lst.append(2)
        lst[0] = 10
        lst[1] = 20
        assert lst[0] == 10
        assert lst[1] == 20

    def test_setitem_out_of_bounds_raises(self):
        lst = ArrayList()
        lst.append(1)
        with pytest.raises(IndexError):
            lst[5] = 10

    def test_delitem(self):
        lst = ArrayList()
        lst.append(1)
        lst.append(2)
        lst.append(3)
        del lst[1]
        assert len(lst) == 2
        assert lst[0] == 1
        assert lst[1] == 3

    def test_delitem_first(self):
        lst = ArrayList()
        lst.append(1)
        lst.append(2)
        del lst[0]
        assert len(lst) == 1
        assert lst[0] == 2

    def test_delitem_last(self):
        lst = ArrayList()
        lst.append(1)
        lst.append(2)
        del lst[1]
        assert len(lst) == 1
        assert lst[0] == 1

    def test_insert_at_beginning(self):
        lst = ArrayList()
        lst.append(2)
        lst.append(3)
        lst.insert(0, 1)
        assert len(lst) == 3
        assert lst[0] == 1
        assert lst[1] == 2
        assert lst[2] == 3

    def test_insert_in_middle(self):
        lst = ArrayList()
        lst.append(1)
        lst.append(3)
        lst.insert(1, 2)
        assert len(lst) == 3
        assert lst[0] == 1
        assert lst[1] == 2
        assert lst[2] == 3

    def test_insert_at_end(self):
        lst = ArrayList()
        lst.append(1)
        lst.append(2)
        lst.insert(2, 3)
        assert len(lst) == 3
        assert lst[2] == 3

    def test_iteration(self):
        lst = ArrayList()
        lst.append(1)
        lst.append(2)
        lst.append(3)
        result = list(lst)
        assert result == [1, 2, 3]

    def test_contains(self):
        lst = ArrayList()
        lst.append(1)
        lst.append(2)
        lst.append(3)
        assert 2 in lst
        assert 5 not in lst
