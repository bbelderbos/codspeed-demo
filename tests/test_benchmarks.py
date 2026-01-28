"""Benchmarks for CodSpeed demo."""

import pytest

from codspeed_demo import (
    bubble_sort,
    fibonacci_iterative,
    fibonacci_recursive,
    find_duplicates_naive,
    find_duplicates_set,
)


# --- Fibonacci benchmarks ---


@pytest.mark.benchmark
def test_fibonacci_recursive_small(benchmark):
    """Benchmark recursive fibonacci with small input."""
    benchmark(fibonacci_recursive, 20)


@pytest.mark.benchmark
def test_fibonacci_iterative_small(benchmark):
    """Benchmark iterative fibonacci with small input."""
    benchmark(fibonacci_iterative, 20)


@pytest.mark.benchmark
def test_fibonacci_iterative_large(benchmark):
    """Benchmark iterative fibonacci with large input."""
    benchmark(fibonacci_iterative, 1000)


# --- Sorting benchmarks ---


@pytest.fixture
def unsorted_list():
    """Generate an unsorted list for benchmarking."""
    import random

    random.seed(42)
    return [random.randint(0, 10000) for _ in range(500)]


@pytest.mark.benchmark
def test_bubble_sort(benchmark, unsorted_list):
    """Benchmark bubble sort."""
    benchmark(bubble_sort, unsorted_list)


# --- Duplicate finding benchmarks ---


@pytest.fixture
def list_with_duplicates():
    """Generate a list with duplicates for benchmarking."""
    import random

    random.seed(42)
    return [random.randint(0, 100) for _ in range(500)]


@pytest.mark.benchmark
def test_find_duplicates_naive(benchmark, list_with_duplicates):
    """Benchmark naive duplicate finding."""
    benchmark(find_duplicates_naive, list_with_duplicates)


@pytest.mark.benchmark
def test_find_duplicates_set(benchmark, list_with_duplicates):
    """Benchmark set-based duplicate finding."""
    benchmark(find_duplicates_set, list_with_duplicates)
