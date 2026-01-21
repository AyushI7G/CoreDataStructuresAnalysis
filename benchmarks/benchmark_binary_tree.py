import time
from structures.binary_tree import BinarySearchTree

def benchmark_bst(n, sorted_insert=False):
    bst = BinarySearchTree()
    values = list(range(n))
    if not sorted_insert:
        import random
        random.shuffle(values)

    start = time.time()
    for v in values:
        bst.insert(v)
    return time.time() - start

if __name__ == "__main__":
    for n in [1_000, 5_000]:
        print(f"Random insert {n}: {benchmark_bst(n):.6f}s")
        print(f"Sorted insert {n}: {benchmark_bst(n, True):.6f}s")
