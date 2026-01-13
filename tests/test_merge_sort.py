"""Tests for merge sort algorithm."""

import pytest
from dsa.sorting.merge_sort import merge_sort


class TestMergeSort:
    """Tests for merge sort."""

    def test_empty_list(self):
        data = []
        merge_sort(data)
        assert data == []

    def test_single_element(self):
        data = [42]
        merge_sort(data)
        assert data == [42]

    def test_two_elements_sorted(self):
        data = [1, 2]
        merge_sort(data)
        assert data == [1, 2]

    def test_two_elements_unsorted(self):
        data = [2, 1]
        merge_sort(data)
        assert data == [1, 2]

    def test_already_sorted(self):
        data = [1, 2, 3, 4, 5]
        merge_sort(data)
        assert data == [1, 2, 3, 4, 5]

    def test_reverse_sorted(self):
        data = [5, 4, 3, 2, 1]
        merge_sort(data)
        assert data == [1, 2, 3, 4, 5]

    def test_random_order(self):
        data = [3, 1, 4, 1, 5, 9, 2, 6]
        merge_sort(data)
        assert data == [1, 1, 2, 3, 4, 5, 6, 9]

    def test_duplicates(self):
        data = [3, 3, 3, 1, 1, 2]
        merge_sort(data)
        assert data == [1, 1, 2, 3, 3, 3]

    def test_negative_numbers(self):
        data = [3, -1, 4, -5, 2]
        merge_sort(data)
        assert data == [-5, -1, 2, 3, 4]

    def test_large_list(self):
        import random
        data = list(range(1000))
        random.shuffle(data)
        merge_sort(data)
        assert data == list(range(1000))

    def test_stability(self):
        """Test that merge sort is stable."""
        # Tuples with same first element should maintain relative order
        data = [(3, 'a'), (1, 'b'), (3, 'c'), (1, 'd'), (2, 'e')]
        # Sort by first element only
        merge_sort(data)
        # Check relative order preserved for equal keys
        threes = [x for x in data if x[0] == 3]
        ones = [x for x in data if x[0] == 1]
        assert threes == [(3, 'a'), (3, 'c')]
        assert ones == [(1, 'b'), (1, 'd')]
