import time
from structures.arrays import DynamicArray

def benchmark_append(n):
    arr = DynamicArray()
    start = time.time()
    for i in range(n):
        arr.append(i)
    return time.time() - start

if __name__ == "__main__":
    for n in [1_000, 10_000, 100_000]:
        t = benchmark_append(n)
        print(f"Append {n} elements: {t:.6f} seconds")
