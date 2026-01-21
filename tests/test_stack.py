from structures.stack import Stack
import pytest

def test_push_pop():
    s = Stack()
    s.push(1)
    s.push(2)
    assert s.pop() == 2
    assert s.pop() == 1

def test_peek():
    s = Stack()
    s.push(10)
    assert s.peek() == 10

def test_pop_empty():
    s = Stack()
    with pytest.raises(IndexError):
        s.pop()
