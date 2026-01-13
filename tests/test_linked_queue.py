"""Tests for LinkedQueue implementation."""

import pytest
from dsa.stacks_queues.linked_queue import LinkedQueue


class TestLinkedQueue:
    """Tests for the LinkedQueue class."""

    def test_new_queue_is_empty(self):
        q = LinkedQueue()
        assert q.is_empty()
        assert len(q) == 0

    def test_enqueue_single_item(self):
        q = LinkedQueue()
        q.enqueue(42)
        assert not q.is_empty()
        assert len(q) == 1
        assert q.front() == 42

    def test_enqueue_dequeue_fifo_order(self):
        q = LinkedQueue()
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        assert q.dequeue() == 1
        assert q.dequeue() == 2
        assert q.dequeue() == 3

    def test_dequeue_empty_raises(self):
        q = LinkedQueue()
        with pytest.raises(IndexError):
            q.dequeue()

    def test_front_empty_raises(self):
        q = LinkedQueue()
        with pytest.raises(IndexError):
            q.front()

    def test_front_does_not_remove(self):
        q = LinkedQueue()
        q.enqueue(99)
        assert q.front() == 99
        assert q.front() == 99
        assert len(q) == 1

    def test_enqueue_dequeue_mixed(self):
        q = LinkedQueue()
        q.enqueue(1)
        q.enqueue(2)
        assert q.dequeue() == 1
        q.enqueue(3)
        assert q.dequeue() == 2
        assert q.dequeue() == 3
        assert q.is_empty()

    def test_many_items(self):
        q = LinkedQueue()
        for i in range(100):
            q.enqueue(i)
        assert len(q) == 100
        for i in range(100):
            assert q.dequeue() == i
        assert q.is_empty()
