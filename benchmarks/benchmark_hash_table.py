import time
import random
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
    keys = list(range(n))
    for k in keys:
        ht.put(k, k)

    start = time.time()
    for k in keys:
        ht.get(k)
    return time.time() - start

if __name__ == "__main__":
    for n in [1_000, 10_000, 100_000]:
        print(f"Insert {n}: {benchmark_insert(n):.6f}s")
        print(f"Lookup {n}: {benchmark_lookup(n):.6f}s")
