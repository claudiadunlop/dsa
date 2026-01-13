"""Tests for elementary sorting algorithms."""

import pytest
from dsa.sorting.elementary import insertion_sort, selection_sort, bubble_sort


class TestInsertionSort:
    """Tests for insertion sort."""

    def test_empty_list(self):
        data = []
        insertion_sort(data)
        assert data == []

    def test_single_element(self):
        data = [42]
        insertion_sort(data)
        assert data == [42]

    def test_already_sorted(self):
        data = [1, 2, 3, 4, 5]
        insertion_sort(data)
        assert data == [1, 2, 3, 4, 5]

    def test_reverse_sorted(self):
        data = [5, 4, 3, 2, 1]
        insertion_sort(data)
        assert data == [1, 2, 3, 4, 5]

    def test_random_order(self):
        data = [3, 1, 4, 1, 5, 9, 2, 6]
        insertion_sort(data)
        assert data == [1, 1, 2, 3, 4, 5, 6, 9]

    def test_duplicates(self):
        data = [3, 3, 3, 1, 1, 2]
        insertion_sort(data)
        assert data == [1, 1, 2, 3, 3, 3]

    def test_negative_numbers(self):
        data = [3, -1, 4, -5, 2]
        insertion_sort(data)
        assert data == [-5, -1, 2, 3, 4]


class TestSelectionSort:
    """Tests for selection sort."""

    def test_empty_list(self):
        data = []
        selection_sort(data)
        assert data == []

    def test_single_element(self):
        data = [42]
        selection_sort(data)
        assert data == [42]

    def test_already_sorted(self):
        data = [1, 2, 3, 4, 5]
        selection_sort(data)
        assert data == [1, 2, 3, 4, 5]

    def test_reverse_sorted(self):
        data = [5, 4, 3, 2, 1]
        selection_sort(data)
        assert data == [1, 2, 3, 4, 5]

    def test_random_order(self):
        data = [3, 1, 4, 1, 5, 9, 2, 6]
        selection_sort(data)
        assert data == [1, 1, 2, 3, 4, 5, 6, 9]

    def test_duplicates(self):
        data = [3, 3, 3, 1, 1, 2]
        selection_sort(data)
        assert data == [1, 1, 2, 3, 3, 3]

    def test_negative_numbers(self):
        data = [3, -1, 4, -5, 2]
        selection_sort(data)
        assert data == [-5, -1, 2, 3, 4]


class TestBubbleSort:
    """Tests for bubble sort."""

    def test_empty_list(self):
        data = []
        bubble_sort(data)
        assert data == []

    def test_single_element(self):
        data = [42]
        bubble_sort(data)
        assert data == [42]

    def test_already_sorted(self):
        data = [1, 2, 3, 4, 5]
        bubble_sort(data)
        assert data == [1, 2, 3, 4, 5]

    def test_reverse_sorted(self):
        data = [5, 4, 3, 2, 1]
        bubble_sort(data)
        assert data == [1, 2, 3, 4, 5]

    def test_random_order(self):
        data = [3, 1, 4, 1, 5, 9, 2, 6]
        bubble_sort(data)
        assert data == [1, 1, 2, 3, 4, 5, 6, 9]

    def test_duplicates(self):
        data = [3, 3, 3, 1, 1, 2]
        bubble_sort(data)
        assert data == [1, 1, 2, 3, 3, 3]

    def test_negative_numbers(self):
        data = [3, -1, 4, -5, 2]
        bubble_sort(data)
        assert data == [-5, -1, 2, 3, 4]
