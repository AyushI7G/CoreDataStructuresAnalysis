# Edge Cases and Failure Scenarios

This document highlights important edge cases and how the implementations handle them.

---

## Dynamic Array
- Appending beyond capacity triggers resizing.
- Deleting from an empty array raises an error.

---

## Linked List
- Deleting the head node.
- Searching in an empty list.

---

## Stack
- Popping from an empty stack raises an exception.

---

## Queue
- Dequeuing from an empty queue.
- Circular queue overflow when capacity is exceeded.

---

## Binary Search Tree
- Sorted insertion causing degeneration.
- Searching in an empty tree.

---

## Hash Table
- Key collisions.
- Deleting non-existent keys.
- Accessing missing keys raises `KeyError`.
