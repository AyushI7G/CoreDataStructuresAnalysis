# Design and Analysis of Core Data Structures Under Realistic Workloads

## Overview

A systematic study of fundamental data structures implemented from first principles, combining empirical benchmarking, correctness verification, and analytical evaluation of performance, scalability, and failure modes under realistic workloads.

## Implemented Data Structures

* Dynamic Arrays
* Singly and Doubly Linked Lists
* Stack (Array-based and Linked List–based)
* Queue (Standard and Circular)
* Binary Search Tree
* Hash Table (Chaining and Open Addressing)

## Key Focus Areas

* Time complexity under different access patterns
* Space utilization and memory overhead
* Edge case handling and failure scenarios
* Performance degradation at scale
* Trade-offs between competing implementations

## Workload Scenarios Tested

* Sequential vs random access
* High insertion vs high lookup workloads
* Small vs large input sizes
* Collision-heavy hash table cases
* Degenerate tree structures

## Project Structure

* `structures/`: Core data structure implementations
* `tests/`: Unit tests validating correctness and edge cases
* `benchmarks/`: Performance benchmarking scripts
* `analysis/`: Written evaluation of time–space trade-offs and failures
* `results/`: Benchmark outputs and summarized findings

## Sample Findings

* Dynamic arrays outperform linked lists in most real-world access patterns despite worse insertion complexity.
* Poor hash functions drastically degrade hash table performance under skewed inputs.
* Unbalanced binary search trees collapse to linear performance without rebalancing.

## Analysis
Detailed discussions on time complexity, space trade-offs, and edge cases are available in the `analysis/` directory.

## How to Run

```bash
pip install -r requirements.txt
python benchmarks/benchmark_hash_table.py
```

## Motivation

While theoretical complexity provides upper bounds, real systems are affected by cache locality, memory allocation, and access patterns. This project explores those practical realities through empirical measurement and structured analysis.

## Future Work

* Add self-balancing trees (AVL, Red-Black)
* Compare custom implementations to standard library equivalents
* Visualize memory usage and cache effects
* Port implementations to a lower-level language for comparison
