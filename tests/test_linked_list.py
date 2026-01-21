from structures.linked_list import SinglyLinkedList

def test_insert_and_search():
    ll = SinglyLinkedList()
    ll.insert(1)
    ll.insert(2)
    assert ll.search(1)
    assert ll.search(2)
    assert not ll.search(3)

def test_delete():
    ll = SinglyLinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.delete(1)
    assert not ll.search(1)
    assert ll.search(2)

def test_delete_head():
    ll = SinglyLinkedList()
    ll.insert(1)
    ll.delete(1)
    assert ll.head is None
