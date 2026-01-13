"""Utilities for timing operations and empirical analysis."""

import time
from typing import Callable, List, Tuple, Any, Optional


def time_operation(operation: Callable[[], Any], trials: int = 5) -> float:
    """Time how long an operation takes to execute.

    Runs the operation multiple times and returns the average time.

    Args:
        operation: A callable that takes no arguments.
        trials: Number of times to run the operation.

    Returns:
        Average execution time in seconds.
    """
    total_time = 0.0
    for _ in range(trials):
        start = time.perf_counter()
        operation()
        end = time.perf_counter()
        total_time += (end - start)
    return total_time / trials


def run_scaling_experiment(
    setup: Callable[[int], Any],
    operation: Callable[[Any], None],
    sizes: List[int],
    trials: int = 5
) -> List[Tuple[int, float]]:
    """Run a scaling experiment across different input sizes.

    For each size n:
        1. Call setup(n) to create the test data
        2. Time how long operation(data) takes
        3. Record the (size, time) pair

    Args:
        setup: Function that takes size n and returns test data.
        operation: Function that takes test data and performs the operation.
        sizes: List of input sizes to test.
        trials: Number of trials per size for averaging.

    Returns:
        List of (size, average_time) tuples.

    Example:
        >>> def setup(n):
        ...     return list(range(n))
        >>> def operation(data):
        ...     data.sort()
        >>> results = run_scaling_experiment(setup, operation, [100, 1000, 10000])
        >>> for size, t in results:
        ...     print(f"n={size}: {t:.6f} seconds")
    """
    results = []
    for n in sizes:
        times = []
        for _ in range(trials):
            data = setup(n)
            start = time.perf_counter()
            operation(data)
            end = time.perf_counter()
            times.append(end - start)
        avg_time = sum(times) / len(times)
        results.append((n, avg_time))
    return results


def print_results(results: List[Tuple[int, float]], label: str = "Operation") -> None:
    """Print timing results in a formatted table.

    Args:
        results: List of (size, time) tuples from run_scaling_experiment.
        label: Label for the operation being timed.
    """
    print(f"\n{label} Timing Results")
    print("-" * 40)
    print(f"{'Size':>10} {'Time (s)':>12} {'Ratio':>10}")
    print("-" * 40)

    prev_time = None
    for size, t in results:
        if prev_time is not None and prev_time > 0:
            ratio = t / prev_time
            print(f"{size:>10} {t:>12.6f} {ratio:>10.2f}")
        else:
            print(f"{size:>10} {t:>12.6f} {'---':>10}")
        prev_time = t


def export_csv(results: List[Tuple[int, float]], filename: str) -> None:
    """Export timing results to a CSV file.

    Args:
        results: List of (size, time) tuples from run_scaling_experiment.
        filename: Path to the output CSV file.
    """
    with open(filename, 'w') as f:
        f.write("size,time_seconds\n")
        for size, t in results:
            f.write(f"{size},{t}\n")
