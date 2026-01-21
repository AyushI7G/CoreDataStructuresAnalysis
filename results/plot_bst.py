import time
import random
import matplotlib.pyplot as plt
from structures.binary_tree import BinarySearchTree

def benchmark(n, sorted_insert):
    bst = BinarySearchTree()
    values = list(range(n))
    if not sorted_insert:
        random.shuffle(values)

    start = time.time()
    for v in values:
        bst.insert(v)
    return time.time() - start

sizes = [500, 1_000, 2_000, 5_000]
random_times = [benchmark(n, False) for n in sizes]
sorted_times = [benchmark(n, True) for n in sizes]

plt.figure()
plt.plot(sizes, random_times, label="Random Insert", marker='o')
plt.plot(sizes, sorted_times, label="Sorted Insert", marker='o')
plt.xlabel("Number of Nodes")
plt.ylabel("Time (seconds)")
plt.title("BST Insertion: Balanced vs Degenerate")
plt.legend()
plt.grid(True)
plt.savefig("results/plots/bst_degenerate.png")
plt.show()
