# CSCI232: Data Structures and Algorithms

This is the central repository for CSCI232: Data Structures and Algorithms. Over the course of the semester, you'll be filling in this API and pushing your modifications to your own branch.

**Reference text:** Goodrich, Tamassia, and Goldwasser, *Data Structures and Algorithms in Python*

## Structure

```
dsa/
├── lists/              # Dynamic arrays and linked lists
├── stacks_queues/      # Stack, queue, and deque implementations
├── trees/              # Binary trees and traversals
├── priority_queues/    # Heap-based priority queue
├── maps/               # Hash maps and tree-based maps
├── sorting/            # Sorting algorithms
└── graphs/             # Graph representations and algorithms
```

## Setup

```bash
# Install in development mode
pip install -e .

# Install with dev dependencies
pip install -e ".[dev]"
```

## Running Tests

```bash
# Run all tests
pytest

# Run tests for a specific module
pytest tests/test_array_stack.py

# Run with verbose output
pytest -v --tb=short
```

## Workflow

1. Implement the methods in each module (replace `raise NotImplementedError`)
2. Run the corresponding tests to verify your implementation
3. Push to GitHub to trigger automated testing

## Pulling Updates

If the instructor pushes updates to the template:

```bash
git remote add upstream <template-repo-url>
git fetch upstream
git merge upstream/main
```
