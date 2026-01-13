"""Tests for ArrayStack implementation."""

import pytest
from dsa.stacks_queues.array_stack import ArrayStack


class TestArrayStack:
    """Tests for the ArrayStack class."""

    def test_new_stack_is_empty(self):
        s = ArrayStack()
        assert s.is_empty()
        assert len(s) == 0

    def test_push_single_item(self):
        s = ArrayStack()
        s.push(42)
        assert not s.is_empty()
        assert len(s) == 1
        assert s.top() == 42

    def test_push_pop_lifo_order(self):
        s = ArrayStack()
        s.push(1)
        s.push(2)
        s.push(3)
        assert s.pop() == 3
        assert s.pop() == 2
        assert s.pop() == 1

    def test_pop_empty_raises(self):
        s = ArrayStack()
        with pytest.raises(IndexError):
            s.pop()

    def test_top_empty_raises(self):
        s = ArrayStack()
        with pytest.raises(IndexError):
            s.top()

    def test_top_does_not_remove(self):
        s = ArrayStack()
        s.push(99)
        assert s.top() == 99
        assert s.top() == 99
        assert len(s) == 1

    def test_push_pop_mixed(self):
        s = ArrayStack()
        s.push(1)
        s.push(2)
        assert s.pop() == 2
        s.push(3)
        assert s.pop() == 3
        assert s.pop() == 1
        assert s.is_empty()

    def test_many_items(self):
        s = ArrayStack()
        for i in range(100):
            s.push(i)
        assert len(s) == 100
        for i in range(99, -1, -1):
            assert s.pop() == i
        assert s.is_empty()
