"""Tests for quick sort algorithm."""

import pytest
from dsa.sorting.quick_sort import quick_sort


class TestQuickSort:
    """Tests for quick sort."""

    def test_empty_list(self):
        data = []
        quick_sort(data)
        assert data == []

    def test_single_element(self):
        data = [42]
        quick_sort(data)
        assert data == [42]

    def test_two_elements_sorted(self):
        data = [1, 2]
        quick_sort(data)
        assert data == [1, 2]

    def test_two_elements_unsorted(self):
        data = [2, 1]
        quick_sort(data)
        assert data == [1, 2]

    def test_already_sorted(self):
        data = [1, 2, 3, 4, 5]
        quick_sort(data)
        assert data == [1, 2, 3, 4, 5]

    def test_reverse_sorted(self):
        data = [5, 4, 3, 2, 1]
        quick_sort(data)
        assert data == [1, 2, 3, 4, 5]

    def test_random_order(self):
        data = [3, 1, 4, 1, 5, 9, 2, 6]
        quick_sort(data)
        assert data == [1, 1, 2, 3, 4, 5, 6, 9]

    def test_duplicates(self):
        data = [3, 3, 3, 1, 1, 2]
        quick_sort(data)
        assert data == [1, 1, 2, 3, 3, 3]

    def test_all_same(self):
        data = [5, 5, 5, 5, 5]
        quick_sort(data)
        assert data == [5, 5, 5, 5, 5]

    def test_negative_numbers(self):
        data = [3, -1, 4, -5, 2]
        quick_sort(data)
        assert data == [-5, -1, 2, 3, 4]

    def test_large_list(self):
        import random
        data = list(range(1000))
        random.shuffle(data)
        quick_sort(data)
        assert data == list(range(1000))

    def test_nearly_sorted(self):
        """Test performance on nearly-sorted data."""
        data = list(range(100))
        # Swap a few elements
        data[10], data[20] = data[20], data[10]
        data[50], data[60] = data[60], data[50]
        quick_sort(data)
        assert data == list(range(100))
