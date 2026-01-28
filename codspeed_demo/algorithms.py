"""Algorithms with varying performance characteristics for benchmarking."""


def fibonacci_recursive(n: int) -> int:
    """Naive recursive fibonacci — exponential time complexity."""
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_iterative(n: int) -> int:
    """Iterative fibonacci — linear time complexity."""
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def bubble_sort(arr: list[int]) -> list[int]:
    """Bubble sort — O(n²) time complexity."""
    result = arr.copy()
    n = len(result)
    for i in range(n):
        for j in range(0, n - i - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
    return result


def find_duplicates_naive(arr: list[int]) -> list[int]:
    """Find duplicates using a set — O(n)."""
    seen = set()
    duplicates = set()
    for item in arr:
        if item in seen:
            duplicates.add(item)
        seen.add(item)
    return list(duplicates)


def find_duplicates_set(arr: list[int]) -> list[int]:
    """Find duplicates using a set — O(n)."""
    seen = set()
    duplicates = set()
    for item in arr:
        if item in seen:
            duplicates.add(item)
        seen.add(item)
    return list(duplicates)
