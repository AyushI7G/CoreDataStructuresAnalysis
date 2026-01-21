import time
import matplotlib.pyplot as plt
from structures.arrays import DynamicArray

def benchmark(n):
    arr = DynamicArray()
    start = time.time()
    for i in range(n):
        arr.append(i)
    return time.time() - start

sizes = [1_000, 5_000, 10_000, 50_000, 100_000]
times = [benchmark(n) for n in sizes]

plt.figure()
plt.plot(sizes, times, marker='o')
plt.xlabel("Number of Elements")
plt.ylabel("Time (seconds)")
plt.title("Dynamic Array Append Performance")
plt.grid(True)
plt.savefig("results/plots/array_append.png")
plt.show()
