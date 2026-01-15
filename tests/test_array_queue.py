"""Tests for ArrayQueue implementation."""

import pytest
from dsa.stacks_queues.array_queue import ArrayQueue


class TestArrayQueue:
    """Tests for the ArrayQueue class."""

    def test_new_queue_is_empty(self):
        q = ArrayQueue()
        assert q.is_empty()
        assert len(q) == 0

    def test_enqueue_single_item(self):
        q = ArrayQueue()
        q.enqueue(42)
        assert not q.is_empty()
        assert len(q) == 1
        assert q.front() == 42

    def test_enqueue_dequeue_fifo_order(self):
        q = ArrayQueue()
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        assert q.dequeue() == 1
        assert q.dequeue() == 2
        assert q.dequeue() == 3

    def test_dequeue_empty_raises(self):
        q = ArrayQueue()
        with pytest.raises(IndexError):
            q.dequeue()

    def test_front_empty_raises(self):
        q = ArrayQueue()
        with pytest.raises(IndexError):
            q.front()

    def test_front_does_not_remove(self):
        q = ArrayQueue()
        q.enqueue(99)
        assert q.front() == 99
        assert q.front() == 99
        assert len(q) == 1

    def test_enqueue_dequeue_mixed(self):
        q = ArrayQueue()
        q.enqueue(1)
        q.enqueue(2)
        assert q.dequeue() == 1
        q.enqueue(3)
        assert q.dequeue() == 2
        assert q.dequeue() == 3
        assert q.is_empty()

    def test_circular_wraparound(self):
        """Test that the circular array properly wraps around."""
        q = ArrayQueue()
        # Fill and partially empty multiple times to test wraparound
        for _ in range(3):
            for i in range(5):
                q.enqueue(i)
            for i in range(5):
                assert q.dequeue() == i

    def test_resize(self):
        """Test that the queue resizes when capacity is exceeded."""
        q = ArrayQueue()
        for i in range(20):
            q.enqueue(i)
        assert len(q) == 20
        for i in range(20):
            assert q.dequeue() == i
