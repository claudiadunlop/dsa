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
# First time only: add the template as a remote
git remote add upstream https://github.com/UMT-CSCI232/dsa.git

# Fetch and merge updates
git fetch upstream
git merge upstream/main --allow-unrelated-histories
```

### Resolving Merge Conflicts

If you've already implemented methods in a file that the instructor updated, Git may report a merge conflict. This is normal and usually easy to resolve.

**Recommended approach:**

1. Use the `-X ours` flag to automatically keep your implementations:
   ```bash
   git merge upstream/main --allow-unrelated-histories -X ours
   ```

2. Check the announcement or commit message for what was added (e.g., a new method stub).

3. Manually copy any new method stubs into your file. The instructor will provide the specific code to add.

4. Stage and commit:
   ```bash
   git add .
   git commit -m "Merged upstream updates"
   ```

**If you need to resolve conflicts manually:**

1. Open the conflicted file and look for conflict markers:
   ```
   <<<<<<< HEAD
   (your code)
   =======
   (upstream code)
   >>>>>>> upstream/main
   ```

2. Edit the file to keep your implementations AND any new additions from upstream.

3. Remove all conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`).

4. Stage and commit:
   ```bash
   git add <filename>
   git commit -m "Resolved merge conflict"
   ```
