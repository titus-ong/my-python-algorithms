import pytest
from my_python_algorithms.data_structures.linked_list import LinkedList, Node


def test_node():
    n = Node(1)
    assert 1 == n.value
    assert None is n.next


def test_empty_ll():
    ll = LinkedList()
    assert None is ll.head


def test_ll_with_head():
    ll = LinkedList(1)
    assert 1 == ll.head.value


def test_append_with_no_head():
    ll = LinkedList()
    ll.append(1)
    assert 1 == ll.head.value


def test_append():
    ll = LinkedList(1)
    ll.append(2)
    assert 2 == ll.head.next.value


def test_indexing_1():
    ll = LinkedList(1)
    assert 1 == ll[0]


def test_indexing_2():
    ll = LinkedList(1)
    ll.append(2)
    assert 2 == ll[1]


def test_indexing_error_1():
    ll = LinkedList()
    with pytest.raises(IndexError):
        ll[0]


def test_indexing_error_2():
    ll = LinkedList(1)
    ll.append(2)
    with pytest.raises(IndexError):
        ll[2]


def test_index():
    ll = LinkedList(1)
    assert 0 == ll.index(1)


def test_index_error_1():
    ll = LinkedList()
    with pytest.raises(ValueError):
        ll.index(1)


def test_index_error_1():
    ll = LinkedList(1)
    with pytest.raises(ValueError):
        ll.index(2)


def test_insert_head():
    ll = LinkedList(1)
    ll.insert(0, "hello")
    assert "hello" == ll[0]


def test_insert_1():
    ll = LinkedList(1)
    ll.append(2)
    ll.append(3)
    ll.insert(1, "hello")
    assert 1 == ll[0]
    assert "hello" == ll[1]
    assert 2 == ll[2]
    assert 3 == ll[3]


def test_insert_2():
    ll = LinkedList(1)
    ll.insert(1, 'hey')
    assert 'hey' == ll[1]


def test_insert_error_1():
    ll = LinkedList()
    with pytest.raises(IndexError):
        ll.insert(1, 1)


def test_insert_error_2():
    ll = LinkedList(1)
    with pytest.raises(IndexError):
        ll.insert(2, 1)


def test_delete_head():
    ll = LinkedList(1)
    ll.delete(0)
    assert None is ll.head


def test_delete_1():
    ll = LinkedList(1)
    ll.append(2)
    ll.delete(0)
    assert 2 == ll[0]
    with pytest.raises(IndexError):
        ll[1]


def test_delete_error_1():
    ll = LinkedList()
    with pytest.raises(IndexError):
        ll.delete(0)


def test_delete_error_2():
    ll = LinkedList(1)
    ll.append(2)
    with pytest.raises(IndexError):
        ll.delete(3)
