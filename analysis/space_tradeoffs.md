# Space Utilization and Trade-offs

This document analyzes memory overhead and space-efficiency trade-offs across different data structures.

---

## Dynamic Array
- Extra unused capacity due to resizing strategy.
- Space complexity: O(n)

**Trade-off:**
Wasted space is exchanged for fast amortized append operations.

---

## Linked List
- Additional memory per node for pointers.
- Space complexity: O(n), with higher constant factors.

**Trade-off:**
Flexible insertion at the cost of higher memory usage and reduced cache efficiency.

---

## Stack and Queue
- Array-based stacks are space-efficient.
- Circular queues avoid shifting costs but require fixed capacity.

---

## Binary Search Tree
- Each node stores two child references.
- Degenerate trees waste memory and computation.

---

## Hash Table
- Buckets introduce overhead.
- Load factor determines memory vs performance balance.

**Trade-off:**
Lower load factors improve speed but increase memory usage.
