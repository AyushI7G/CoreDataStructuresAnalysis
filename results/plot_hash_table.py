import time
import random
import matplotlib.pyplot as plt
from structures.hash_table import HashTable

def benchmark_insert(n):
    ht = HashTable()
    keys = [random.randint(0, 10**7) for _ in range(n)]
    start = time.time()
    for k in keys:
        ht.put(k, k)
    return time.time() - start

def benchmark_lookup(n):
    ht = HashTable()
    for i in range(n):
        ht.put(i, i)
    start = time.time()
    for i in range(n):
        ht.get(i)
    return time.time() - start

sizes = [1_000, 5_000, 10_000, 50_000]
insert_times = [benchmark_insert(n) for n in sizes]
lookup_times = [benchmark_lookup(n) for n in sizes]

plt.figure()
plt.plot(sizes, insert_times, label="Insert", marker='o')
plt.plot(sizes, lookup_times, label="Lookup", marker='o')
plt.xlabel("Number of Elements")
plt.ylabel("Time (seconds)")
plt.title("Hash Table Performance")
plt.legend()
plt.grid(True)
plt.savefig("results/plots/hash_table.png")
plt.show()
