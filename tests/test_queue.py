from structures.queue import Queue, CircularQueue
import pytest

def test_queue_enqueue_dequeue():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    assert q.dequeue() == 1
    assert q.dequeue() == 2

def test_queue_empty():
    q = Queue()
    with pytest.raises(IndexError):
        q.dequeue()

def test_circular_queue():
    cq = CircularQueue(3)
    cq.enqueue(1)
    cq.enqueue(2)
    cq.enqueue(3)
    assert cq.dequeue() == 1
    cq.enqueue(4)
    assert cq.dequeue() == 2
