"""Tests for binary search algorithm."""

import pytest
from dsa.search.binary_search import (
    binary_search,
    binary_search_recursive,
    bisect_left,
    bisect_right,
)


class TestBinarySearch:
    """Tests for iterative binary search."""

    def test_empty_list(self):
        assert binary_search([], 5) is None

    def test_single_element_found(self):
        assert binary_search([5], 5) == 0

    def test_single_element_not_found(self):
        assert binary_search([5], 3) is None

    def test_first_element(self):
        assert binary_search([1, 2, 3, 4, 5], 1) == 0

    def test_last_element(self):
        assert binary_search([1, 2, 3, 4, 5], 5) == 4

    def test_middle_element(self):
        assert binary_search([1, 2, 3, 4, 5], 3) == 2

    def test_not_found_too_small(self):
        assert binary_search([1, 2, 3, 4, 5], 0) is None

    def test_not_found_too_large(self):
        assert binary_search([1, 2, 3, 4, 5], 6) is None

    def test_not_found_in_gap(self):
        assert binary_search([1, 3, 5, 7, 9], 4) is None

    def test_even_length_list(self):
        assert binary_search([1, 2, 3, 4], 3) == 2

    def test_negative_numbers(self):
        assert binary_search([-5, -3, -1, 0, 2], -3) == 1

    def test_duplicates_finds_one(self):
        # Should find one of the matching indices (exact index unspecified)
        result = binary_search([1, 2, 2, 2, 3], 2)
        assert result in [1, 2, 3]

    def test_large_list(self):
        data = list(range(0, 10000, 2))  # Even numbers 0-9998
        assert binary_search(data, 5000) == 2500
        assert binary_search(data, 5001) is None


class TestBinarySearchRecursive:
    """Tests for recursive binary search."""

    def test_empty_list(self):
        assert binary_search_recursive([], 5) is None

    def test_single_element_found(self):
        assert binary_search_recursive([5], 5) == 0

    def test_single_element_not_found(self):
        assert binary_search_recursive([5], 3) is None

    def test_first_element(self):
        assert binary_search_recursive([1, 2, 3, 4, 5], 1) == 0

    def test_last_element(self):
        assert binary_search_recursive([1, 2, 3, 4, 5], 5) == 4

    def test_middle_element(self):
        assert binary_search_recursive([1, 2, 3, 4, 5], 3) == 2

    def test_not_found(self):
        assert binary_search_recursive([1, 2, 3, 4, 5], 6) is None

    def test_negative_numbers(self):
        assert binary_search_recursive([-5, -3, -1, 0, 2], -1) == 2


class TestBisectLeft:
    """Tests for bisect_left (leftmost insertion point)."""

    def test_empty_list(self):
        assert bisect_left([], 5) == 0

    def test_insert_at_beginning(self):
        assert bisect_left([2, 4, 6], 1) == 0

    def test_insert_at_end(self):
        assert bisect_left([2, 4, 6], 7) == 3

    def test_insert_in_middle(self):
        assert bisect_left([2, 4, 6], 3) == 1

    def test_existing_element(self):
        assert bisect_left([2, 4, 6], 4) == 1

    def test_duplicates_returns_leftmost(self):
        assert bisect_left([1, 2, 2, 2, 3], 2) == 1

    def test_all_same_elements(self):
        assert bisect_left([5, 5, 5, 5], 5) == 0


class TestBisectRight:
    """Tests for bisect_right (rightmost insertion point)."""

    def test_empty_list(self):
        assert bisect_right([], 5) == 0

    def test_insert_at_beginning(self):
        assert bisect_right([2, 4, 6], 1) == 0

    def test_insert_at_end(self):
        assert bisect_right([2, 4, 6], 7) == 3

    def test_insert_in_middle(self):
        assert bisect_right([2, 4, 6], 3) == 1

    def test_existing_element(self):
        assert bisect_right([2, 4, 6], 4) == 2

    def test_duplicates_returns_rightmost(self):
        assert bisect_right([1, 2, 2, 2, 3], 2) == 4

    def test_all_same_elements(self):
        assert bisect_right([5, 5, 5, 5], 5) == 4
