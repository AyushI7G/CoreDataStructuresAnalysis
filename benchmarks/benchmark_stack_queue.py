import time
from structures.stack import Stack
from structures.queue import Queue

def benchmark_stack(n):
    s = Stack()
    start = time.time()
    for i in range(n):
        s.push(i)
    for i in range(n):
        s.pop()
    return time.time() - start

def benchmark_queue(n):
    q = Queue()
    start = time.time()
    for i in range(n):
        q.enqueue(i)
    for i in range(n):
        q.dequeue()
    return time.time() - start

if __name__ == "__main__":
    for n in [1_000, 10_000]:
        print(f"Stack ops {n}: {benchmark_stack(n):.6f}s")
        print(f"Queue ops {n}: {benchmark_queue(n):.6f}s")
