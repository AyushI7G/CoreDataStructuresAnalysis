from structures.hash_table import HashTable
import pytest

def test_put_get():
    ht = HashTable()
    ht.put("a", 1)
    ht.put("b", 2)
    assert ht.get("a") == 1
    assert ht.get("b") == 2

def test_update_value():
    ht = HashTable()
    ht.put("a", 1)
    ht.put("a", 2)
    assert ht.get("a") == 2

def test_delete():
    ht = HashTable()
    ht.put("a", 1)
    ht.delete("a")
    with pytest.raises(KeyError):
        ht.get("a")

def test_missing_key():
    ht = HashTable()
    with pytest.raises(KeyError):
        ht.get("x")
