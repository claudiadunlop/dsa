"""Tests for heap sort algorithm."""

import pytest
from dsa.sorting.heap_sort import heap_sort


class TestHeapSort:
    """Tests for heap sort."""

    def test_empty_list(self):
        data = []
        heap_sort(data)
        assert data == []

    def test_single_element(self):
        data = [42]
        heap_sort(data)
        assert data == [42]

    def test_two_elements_sorted(self):
        data = [1, 2]
        heap_sort(data)
        assert data == [1, 2]

    def test_two_elements_unsorted(self):
        data = [2, 1]
        heap_sort(data)
        assert data == [1, 2]

    def test_already_sorted(self):
        data = [1, 2, 3, 4, 5]
        heap_sort(data)
        assert data == [1, 2, 3, 4, 5]

    def test_reverse_sorted(self):
        data = [5, 4, 3, 2, 1]
        heap_sort(data)
        assert data == [1, 2, 3, 4, 5]

    def test_random_order(self):
        data = [3, 1, 4, 1, 5, 9, 2, 6]
        heap_sort(data)
        assert data == [1, 1, 2, 3, 4, 5, 6, 9]

    def test_duplicates(self):
        data = [3, 3, 3, 1, 1, 2]
        heap_sort(data)
        assert data == [1, 1, 2, 3, 3, 3]

    def test_all_same(self):
        data = [5, 5, 5, 5, 5]
        heap_sort(data)
        assert data == [5, 5, 5, 5, 5]

    def test_negative_numbers(self):
        data = [3, -1, 4, -5, 2]
        heap_sort(data)
        assert data == [-5, -1, 2, 3, 4]

    def test_large_list(self):
        import random
        data = list(range(1000))
        random.shuffle(data)
        heap_sort(data)
        assert data == list(range(1000))
