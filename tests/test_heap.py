"""Tests for Heap (priority queue) implementation."""

import pytest
from dsa.priority_queues.heap import Heap


class TestHeap:
    """Tests for the Heap class."""

    def test_new_heap_is_empty(self):
        h = Heap()
        assert h.is_empty()
        assert len(h) == 0

    def test_add_single_item(self):
        h = Heap()
        h.add(5, "five")
        assert not h.is_empty()
        assert len(h) == 1
        assert h.min() == (5, "five")

    def test_add_maintains_min_property(self):
        h = Heap()
        h.add(3, "three")
        h.add(1, "one")
        h.add(2, "two")
        assert h.min() == (1, "one")

    def test_remove_min_returns_minimum(self):
        h = Heap()
        h.add(3, "three")
        h.add(1, "one")
        h.add(2, "two")
        assert h.remove_min() == (1, "one")
        assert h.remove_min() == (2, "two")
        assert h.remove_min() == (3, "three")

    def test_min_empty_raises(self):
        h = Heap()
        with pytest.raises(IndexError):
            h.min()

    def test_remove_min_empty_raises(self):
        h = Heap()
        with pytest.raises(IndexError):
            h.remove_min()

    def test_min_does_not_remove(self):
        h = Heap()
        h.add(1, "one")
        assert h.min() == (1, "one")
        assert h.min() == (1, "one")
        assert len(h) == 1

    def test_add_remove_mixed(self):
        h = Heap()
        h.add(5, "five")
        h.add(3, "three")
        assert h.remove_min() == (3, "three")
        h.add(1, "one")
        assert h.remove_min() == (1, "one")
        assert h.remove_min() == (5, "five")
        assert h.is_empty()

    def test_duplicate_keys(self):
        h = Heap()
        h.add(1, "first")
        h.add(1, "second")
        h.add(1, "third")
        # All have the same key, so any order is valid
        results = [h.remove_min(), h.remove_min(), h.remove_min()]
        keys = [r[0] for r in results]
        assert keys == [1, 1, 1]

    def test_many_items(self):
        h = Heap()
        import random
        values = list(range(100))
        random.shuffle(values)
        for v in values:
            h.add(v, str(v))
        assert len(h) == 100
        for i in range(100):
            key, value = h.remove_min()
            assert key == i
        assert h.is_empty()

    def test_negative_keys(self):
        h = Heap()
        h.add(0, "zero")
        h.add(-1, "negative")
        h.add(1, "positive")
        assert h.min() == (-1, "negative")
