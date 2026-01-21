from structures.binary_tree import BinarySearchTree

def test_insert_and_search():
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)

    assert bst.search(10)
    assert bst.search(5)
    assert bst.search(15)
    assert not bst.search(20)

def test_inorder_traversal():
    bst = BinarySearchTree()
    for value in [10, 5, 15, 3]:
        bst.insert(value)

    assert bst.inorder() == [3, 5, 10, 15]
