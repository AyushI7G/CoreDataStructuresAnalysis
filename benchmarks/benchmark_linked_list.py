import time
from structures.linked_list import SinglyLinkedList

def benchmark_insert(n):
    ll = SinglyLinkedList()
    start = time.time()
    for i in range(n):
        ll.insert(i)
    return time.time() - start

def benchmark_search(n):
    ll = SinglyLinkedList()
    for i in range(n):
        ll.insert(i)

    start = time.time()
    for i in range(n):
        ll.search(i)
    return time.time() - start

if __name__ == "__main__":
    for n in [1_000, 10_000]:
        print(f"Insert {n}: {benchmark_insert(n):.6f}s")
        print(f"Search {n}: {benchmark_search(n):.6f}s")
