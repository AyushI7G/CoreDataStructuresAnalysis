# Time Complexity Analysis

This document compares the theoretical time complexity of core data structures with their observed behavior under realistic workloads.

---

## Dynamic Array
- Append: Amortized O(1)
- Insert/Delete (middle): O(n)

**Observation:**
Benchmarks show that append operations scale nearly linearly with input size, validating amortized O(1) behavior. Occasional spikes occur during resizing, but their cost is spread across many operations.

---

## Linked List
- Insert (end): O(n)
- Search: O(n)

**Observation:**
Traversal dominates performance. Despite constant-time node insertion, overall performance is limited by linear traversal cost and poor cache locality.

---

## Stack
- Push/Pop: O(1)

**Observation:**
Stack operations remain consistently fast across all input sizes due to contiguous memory usage and minimal overhead.

---

## Queue
- Enqueue: O(1)
- Dequeue (array-based): O(n)

**Observation:**
Using a Python list for dequeue results in linear time due to element shifting. This motivates circular queues or deque-based implementations.

---

## Binary Search Tree
- Insert/Search: Average O(log n), Worst O(n)

**Observation:**
Random insertions behave close to logarithmic time, while sorted insertions cause tree degeneration, leading to linear performance.

---

## Hash Table
- Insert/Search: Average O(1), Worst O(n)

**Observation:**
With a reasonable hash distribution, performance remains near constant. Poor hash distribution significantly degrades performance due to collision chains.
