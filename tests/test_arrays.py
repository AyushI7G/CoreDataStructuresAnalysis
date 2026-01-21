from structures.stack import DynamicArray
import pytest

def test_append():
    arr = DynamicArray()
    arr.append(1)
    arr.append(2)
    assert arr.size == 2
    assert arr.data[0] == 1
    assert arr.data[1] == 2

def test_insert():
    arr = DynamicArray()
    arr.append(1)
    arr.append(3)
    arr.insert(1, 2)
    assert arr.data[1] == 2

def test_delete():
    arr = DynamicArray()
    arr.append(1)
    arr.append(2)
    arr.delete(0)
    assert arr.size == 1
    assert arr.data[0] == 2

def test_delete_invalid_index():
    arr = DynamicArray()
    with pytest.raises(IndexError):
        arr.delete(0)
