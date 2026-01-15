"""Tests for ArrayDeque implementation."""

import pytest
from dsa.stacks_queues.deque import ArrayDeque


class TestArrayDeque:
    """Tests for the ArrayDeque class."""

    def test_new_deque_is_empty(self):
        d = ArrayDeque()
        assert d.is_empty()
        assert len(d) == 0

    def test_add_first(self):
        d = ArrayDeque()
        d.add_first(1)
        d.add_first(2)
        d.add_first(3)
        assert len(d) == 3
        assert d.first() == 3
        assert d.last() == 1

    def test_add_last(self):
        d = ArrayDeque()
        d.add_last(1)
        d.add_last(2)
        d.add_last(3)
        assert len(d) == 3
        assert d.first() == 1
        assert d.last() == 3

    def test_remove_first(self):
        d = ArrayDeque()
        d.add_last(1)
        d.add_last(2)
        d.add_last(3)
        assert d.remove_first() == 1
        assert d.remove_first() == 2
        assert d.remove_first() == 3

    def test_remove_last(self):
        d = ArrayDeque()
        d.add_last(1)
        d.add_last(2)
        d.add_last(3)
        assert d.remove_last() == 3
        assert d.remove_last() == 2
        assert d.remove_last() == 1

    def test_remove_first_empty_raises(self):
        d = ArrayDeque()
        with pytest.raises(IndexError):
            d.remove_first()

    def test_remove_last_empty_raises(self):
        d = ArrayDeque()
        with pytest.raises(IndexError):
            d.remove_last()

    def test_first_empty_raises(self):
        d = ArrayDeque()
        with pytest.raises(IndexError):
            d.first()

    def test_last_empty_raises(self):
        d = ArrayDeque()
        with pytest.raises(IndexError):
            d.last()

    def test_first_does_not_remove(self):
        d = ArrayDeque()
        d.add_last(99)
        assert d.first() == 99
        assert d.first() == 99
        assert len(d) == 1

    def test_last_does_not_remove(self):
        d = ArrayDeque()
        d.add_first(99)
        assert d.last() == 99
        assert d.last() == 99
        assert len(d) == 1

    def test_mixed_operations(self):
        d = ArrayDeque()
        d.add_first(2)
        d.add_first(1)
        d.add_last(3)
        d.add_last(4)
        assert d.remove_first() == 1
        assert d.remove_last() == 4
        assert d.first() == 2
        assert d.last() == 3

    def test_use_as_stack(self):
        """Deque can function as a stack using add_last/remove_last."""
        d = ArrayDeque()
        d.add_last(1)
        d.add_last(2)
        d.add_last(3)
        assert d.remove_last() == 3
        assert d.remove_last() == 2
        assert d.remove_last() == 1

    def test_use_as_queue(self):
        """Deque can function as a queue using add_last/remove_first."""
        d = ArrayDeque()
        d.add_last(1)
        d.add_last(2)
        d.add_last(3)
        assert d.remove_first() == 1
        assert d.remove_first() == 2
        assert d.remove_first() == 3
