# DSA Course Repository Specification

A specification for a Python data structures and algorithms course repository, designed for use with GitHub Classroom and automated testing.

## Overview

This repository serves as a template for an intermediate (200-level) data structures and algorithms course. Students receive their own private copy and implement methods over the course of the semester. Unit tests run automatically on push via GitHub Actions.

**Reference text:** Goodrich, Tamassia, and Goldwasser, *Data Structures and Algorithms in Python* (used as reference, not followed strictly)

**Class size:** ~25 students

---

## Design Principles

1. **Pure Python:** Avoid custom libraries and frameworks. Use built-in exceptions (`IndexError`, `KeyError`) rather than custom exception classes. Students should learn standard Python conventions.

2. **Strict ABCs:** Use Python's `abc` module with `@abstractmethod` decorators to enforce interface compliance. Subclasses that fail to implement required methods raise `TypeError` at instantiation.

3. **One file per concrete data structure:** Keeps imports simple and reduces merge conflicts when students pull upstream updates. Node classes can be inner classes within the data structure file.

4. **Layered implementations:** Later structures build on earlier ones (e.g., `Queue` uses student's `LinkedList`). This makes the course feel cohesive but requires careful sequencing.

5. **Separate base classes:** Each topic folder has a `base.py` containing provided abstract base classes. Students implement concrete subclasses in separate files.

6. **No Jupyter notebooks:** Encourages proper software development practices and simplifies version control.

7. **Full test visibility:** Students see all tests from day one. Separate assessments verify understanding away from the computer.

---

## Directory Structure

```
dsa-course/
├── README.md
├── pyproject.toml
├── dsa/
│   ├── __init__.py
│   │
│   ├── lists/
│   │   ├── __init__.py
│   │   ├── base.py              # PROVIDED: Sequence ABC
│   │   ├── array_list.py        # STUDENT: dynamic array implementation
│   │   └── linked_list.py       # STUDENT: singly/doubly linked
│   │
│   ├── stacks_queues/
│   │   ├── __init__.py
│   │   ├── base.py              # PROVIDED: Stack, Queue, Deque ABCs
│   │   ├── array_stack.py       # STUDENT
│   │   ├── linked_stack.py      # STUDENT
│   │   ├── array_queue.py       # STUDENT
│   │   ├── linked_queue.py      # STUDENT
│   │   └── deque.py             # STUDENT
│   │
│   ├── trees/
│   │   ├── __init__.py
│   │   ├── base.py              # PROVIDED: Tree, BinaryTree ABCs
│   │   ├── linked_binary_tree.py    # STUDENT
│   │   └── traversals.py        # STUDENT: pre/in/post/level-order
│   │
│   ├── priority_queues/
│   │   ├── __init__.py
│   │   ├── base.py              # PROVIDED: PriorityQueue ABC
│   │   └── heap.py              # STUDENT: binary heap
│   │
│   ├── maps/
│   │   ├── __init__.py
│   │   ├── base.py              # PROVIDED: Map ABC
│   │   ├── hash_map.py          # STUDENT: separate chaining or probing
│   │   ├── bst_map.py           # STUDENT: unbalanced BST
│   │   └── rb_tree_map.py       # STUDENT: red-black tree
│   │
│   ├── sorting/
│   │   ├── __init__.py
│   │   ├── elementary.py        # STUDENT: insertion, selection, bubble
│   │   ├── merge_sort.py        # STUDENT
│   │   ├── quick_sort.py        # STUDENT
│   │   └── heap_sort.py         # STUDENT
│   │
│   └── graphs/
│       ├── __init__.py
│       ├── base.py              # PROVIDED: Graph ABC
│       ├── adjacency_map.py     # STUDENT: graph representation
│       ├── traversals.py        # STUDENT: DFS and BFS (same file)
│       ├── mst.py               # STUDENT: Prim/Kruskal
│       └── shortest_paths.py    # STUDENT: Dijkstra, possibly Bellman-Ford
│
├── tests/
│   ├── test_array_list.py
│   ├── test_linked_list.py
│   ├── test_array_stack.py
│   ├── test_linked_stack.py
│   ├── test_array_queue.py
│   ├── test_linked_queue.py
│   ├── test_deque.py
│   ├── test_linked_binary_tree.py
│   ├── test_traversals.py
│   ├── test_heap.py
│   ├── test_hash_map.py
│   ├── test_bst_map.py
│   ├── test_rb_tree_map.py
│   ├── test_elementary_sorts.py
│   ├── test_merge_sort.py
│   ├── test_quick_sort.py
│   ├── test_heap_sort.py
│   ├── test_adjacency_map.py
│   ├── test_graph_traversals.py
│   ├── test_mst.py
│   └── test_shortest_paths.py
│
├── benchmarks/
│   ├── __init__.py
│   └── timing.py                # PROVIDED: utilities for timing, plotting
│
└── .github/
    └── workflows/
        └── ci.yml
```

---

## Base Class Conventions

### General Pattern

- Use `abc.ABC` and `@abstractmethod`
- Use `typing.Generic[T]` for element types (or `Generic[K, V]` for maps)
- Class docstring includes:
  - Brief description of the ADT
  - List of core operations with expected time complexities
  - Any important semantic notes
- Method docstrings include:
  - Args, Returns, Raises sections
  - Brief description of behavior
- Provide concrete implementations for convenience methods that don't involve implementation choice (e.g., `is_empty()` calls `__len__()`)
- Use Python's dunder methods where appropriate (`__len__`, `__getitem__`, `__iter__`, etc.)

### Reference Example: Stack

```python
"""Abstract base class defining the stack interface."""

from abc import ABC, abstractmethod
from typing import TypeVar, Generic

T = TypeVar('T')


class Stack(ABC, Generic[T]):
    """A last-in, first-out (LIFO) collection.
    
    A stack supports insertion and removal only at one end, called the "top."
    The most recently added element is always the first to be removed.
    
    Core operations and their expected time complexities:
        push(item)  - Add item to top           O(1) amortized or worst-case
        pop()       - Remove and return top     O(1)
        top()       - Return top without removing   O(1)
        is_empty()  - Check if stack is empty   O(1)
        __len__()   - Return number of items    O(1)
    """
    
    @abstractmethod
    def push(self, item: T) -> None:
        """Add an item to the top of the stack.
        
        Args:
            item: The element to add.
        """
        pass
    
    @abstractmethod
    def pop(self) -> T:
        """Remove and return the item at the top of the stack.
        
        Returns:
            The most recently added item.
        
        Raises:
            IndexError: If the stack is empty.
        """
        pass
    
    @abstractmethod
    def top(self) -> T:
        """Return the item at the top without removing it.
        
        Returns:
            The most recently added item.
        
        Raises:
            IndexError: If the stack is empty.
        """
        pass
    
    def is_empty(self) -> bool:
        """Return True if the stack contains no items.
        
        This default implementation relies on __len__. Subclasses may
        override for efficiency if needed.
        """
        return len(self) == 0
    
    @abstractmethod
    def __len__(self) -> int:
        """Return the number of items in the stack."""
        pass
```

### Reference Example: Map

```python
"""Abstract base class defining the map (associative array) interface."""

from abc import ABC, abstractmethod
from typing import TypeVar, Generic, Iterator, Tuple

K = TypeVar('K')
V = TypeVar('V')


class Map(ABC, Generic[K, V]):
    """A collection of key-value pairs with unique keys.
    
    A map (also called associative array, dictionary, or symbol table)
    associates keys with values. Each key appears at most once; inserting
    a duplicate key overwrites the previous value.
    
    Core operations and their expected time complexities vary by
    implementation:
    
                        Hash-based      Tree-based (balanced)
        __getitem__     O(1) avg        O(log n)
        __setitem__     O(1) avg        O(log n)
        __delitem__     O(1) avg        O(log n)
        __contains__    O(1) avg        O(log n)
        __len__         O(1)            O(1)
        __iter__        O(n)            O(n)
    
    This interface uses Python's bracket syntax for access:
        m[key] = value   calls __setitem__
        value = m[key]   calls __getitem__
        del m[key]       calls __delitem__
        key in m         calls __contains__
    """
    
    @abstractmethod
    def __getitem__(self, key: K) -> V:
        """Return the value associated with key.
        
        Args:
            key: The key to look up.
            
        Returns:
            The value associated with the key.
            
        Raises:
            KeyError: If the key is not found.
        """
        pass
    
    @abstractmethod
    def __setitem__(self, key: K, value: V) -> None:
        """Associate value with key, overwriting any existing value.
        
        Args:
            key: The key to insert or update.
            value: The value to associate with the key.
        """
        pass
    
    @abstractmethod
    def __delitem__(self, key: K) -> None:
        """Remove the key and its associated value.
        
        Args:
            key: The key to remove.
            
        Raises:
            KeyError: If the key is not found.
        """
        pass
    
    @abstractmethod
    def __contains__(self, key: K) -> bool:
        """Return True if the key is in the map.
        
        Args:
            key: The key to search for.
        """
        pass
    
    @abstractmethod
    def __len__(self) -> int:
        """Return the number of key-value pairs in the map."""
        pass
    
    @abstractmethod
    def __iter__(self) -> Iterator[K]:
        """Iterate over keys in the map.
        
        The iteration order depends on the implementation:
        - Hash-based: arbitrary order
        - Tree-based: sorted order by key (not strictly required)
        
        Yields:
            Each key in the map.
        """
        pass
    
    def is_empty(self) -> bool:
        """Return True if the map contains no key-value pairs."""
        return len(self) == 0
    
    def get(self, key: K, default: V = None) -> V:
        """Return the value for key if present, else default.
        
        Unlike __getitem__, this does not raise KeyError for missing keys.
        
        Args:
            key: The key to look up.
            default: Value to return if key is not found.
            
        Returns:
            The associated value, or default if key is absent.
        """
        try:
            return self[key]
        except KeyError:
            return default
    
    def keys(self) -> Iterator[K]:
        """Return an iterator over the map's keys.
        
        Equivalent to iter(self).
        """
        return iter(self)
    
    def values(self) -> Iterator[V]:
        """Return an iterator over the map's values."""
        for key in self:
            yield self[key]
    
    def items(self) -> Iterator[Tuple[K, V]]:
        """Return an iterator over (key, value) pairs."""
        for key in self:
            yield (key, self[key])
```

### Notes for Other Base Classes

- **Queue/Deque:** Similar to Stack. Queue has `enqueue`/`dequeue`/`front`. Deque adds `add_first`/`add_last`/`remove_first`/`remove_last`.
- **List (Sequence):** Define `__getitem__`, `__setitem__`, `__delitem__`, `__len__`, `insert`, `append`. Avoid inheriting from `collections.abc.MutableSequence`.
- **Tree/BinaryTree:** More complex. Consider methods like `root()`, `parent(p)`, `children(p)`, `is_leaf(p)`, `num_children(p)`. BinaryTree adds `left(p)`, `right(p)`. Position-based interface (as in Goodrich) or node-based.
- **PriorityQueue:** `add(key, value)`, `min()`, `remove_min()`, `__len__`, `is_empty()`.
- **Graph:** `vertex_count()`, `edge_count()`, `vertices()`, `edges()`, `get_edge(u, v)`, `degree(v)`, `incident_edges(v)`, `insert_vertex(x)`, `insert_edge(u, v, x)`, `remove_vertex(v)`, `remove_edge(e)`.

---

## Student Implementation Files

Student files should:

1. Import the base class from the same folder's `base.py`
2. Define a concrete class that inherits from the ABC
3. Implement all abstract methods
4. Use `raise NotImplementedError` as placeholder in the template

Example stub for `array_stack.py`:

```python
"""Array-based stack implementation."""

from dsa.stacks_queues.base import Stack
from typing import TypeVar

T = TypeVar('T')


class ArrayStack(Stack[T]):
    """Stack implementation using a Python list as underlying storage."""
    
    def __init__(self):
        """Create an empty stack."""
        raise NotImplementedError
    
    def push(self, item: T) -> None:
        raise NotImplementedError
    
    def pop(self) -> T:
        raise NotImplementedError
    
    def top(self) -> T:
        raise NotImplementedError
    
    def __len__(self) -> int:
        raise NotImplementedError
```

---

## Testing

### Framework

Use **pytest**. One test file per concrete class.

### Test File Pattern

```python
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
```

### Running Tests

```bash
# All tests
pytest

# Single file
pytest tests/test_array_stack.py

# Specific test
pytest -k "test_push_pop"

# Verbose output
pytest -v --tb=short
```

---

## GitHub Actions CI

File: `.github/workflows/ci.yml`

```yaml
name: Run Tests

on:
  push:
    branches: ["*"]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
      - name: Check out code
        uses: actions/checkout@v4
      
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install pytest
          pip install -e .
      
      - name: Run tests
        run: pytest --tb=short
```

Students see a green check or red X next to each commit on GitHub. Clicking shows full pytest output.

---

## GitHub Classroom Setup

1. **Create a GitHub Organization** for the course (e.g., `cs200-fall2025`)

2. **Create the template repository** with all provided files (base classes, test files, CI workflow, pyproject.toml)

3. **In GitHub Classroom:**
   - Create an assignment linked to the template repo
   - Configure as individual assignment, private repos
   - Share the assignment link with students

4. **Student workflow:**
   - Click assignment link → gets private repo in the org
   - Clone locally, implement methods, push
   - CI runs automatically, shows pass/fail

5. **Upstream updates:** Students add the template as a remote to pull corrections:
   ```bash
   git remote add upstream https://github.com/cs200-fall2025/dsa-template.git
   git fetch upstream
   git merge upstream/main
   ```

---

## pyproject.toml

```toml
[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[project]
name = "dsa"
version = "0.1.0"
description = "Data Structures and Algorithms course implementations"
requires-python = ">=3.10"

[project.optional-dependencies]
dev = ["pytest>=7.0"]

[tool.setuptools.packages.find]
where = ["."]
```

---

## Benchmarking Component

For empirical analysis assignments, provide timing utilities in `benchmarks/timing.py`:

- Function to time operations across varying input sizes
- Simple plotting with matplotlib (or output CSV for students to plot themselves)
- Students write scripts that use their implementations and produce performance graphs
- Compare empirical results to theoretical complexity predictions

---

## Summary of What's Provided vs. Student-Implemented

| Folder | Provided | Student Implements |
|--------|----------|-------------------|
| lists | `base.py` (Sequence ABC) | `array_list.py`, `linked_list.py` |
| stacks_queues | `base.py` (Stack, Queue, Deque ABCs) | `array_stack.py`, `linked_stack.py`, `array_queue.py`, `linked_queue.py`, `deque.py` |
| trees | `base.py` (Tree, BinaryTree ABCs) | `linked_binary_tree.py`, `traversals.py` |
| priority_queues | `base.py` (PriorityQueue ABC) | `heap.py` |
| maps | `base.py` (Map ABC) | `hash_map.py`, `bst_map.py`, `rb_tree_map.py` |
| sorting | — | `elementary.py`, `merge_sort.py`, `quick_sort.py`, `heap_sort.py` |
| graphs | `base.py` (Graph ABC) | `adjacency_map.py`, `traversals.py`, `mst.py`, `shortest_paths.py` |
| benchmarks | `timing.py` | — |
| tests | All test files | — |
