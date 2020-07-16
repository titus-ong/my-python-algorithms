import pytest
from my_python_algorithms.data_structures.doubly_linked_list import DoublyLinkedList as Dll, Node


def test_node():
    n = Node(1)
    assert 1 == n.value
    assert None is n.prev
    assert None is n.next


def test_dll_no_head():
    dll = Dll()
    assert None is dll.head


def test_dll_head():
    dll = Dll(1)
    assert 1 == dll.head.value


def test_append_head():
    dll = Dll()
    dll.append(1)
    assert 1 == dll.head.value


def test_append():
    dll = Dll(0)
    dll.append(1)
    assert 1 == dll.head.next.value
    assert 0 == dll.head.next.prev.value


def test_indexing_1():
    dll = Dll(0)
    dll.append(1)
    assert 0 == dll[0]
    assert 1 == dll[1]


def test_indexing_error_1():
    dll = Dll()
    with pytest.raises(IndexError):
        dll[0]


def test_indexing_error_2():
    dll = Dll(0)
    dll.append(1)
    with pytest.raises(IndexError):
        dll[2]


def test_index_head():
    dll = Dll(1)
    assert 0 == dll.index(1)


def test_index():
    dll = Dll(0)
    dll.append(1)
    assert 1 == dll.index(1)


def test_index_error_1():
    dll = Dll()
    with pytest.raises(ValueError):
        dll.index(0)


def test_index_error_2():
    dll = Dll(0)
    dll.append(1)
    with pytest.raises(ValueError):
        dll.index(2)


def test_insert_head():
    dll = Dll()
    dll.insert(0, "hey")
    assert "hey" == dll[0]


def test_insert_head_2():
    dll = Dll(1)
    dll.insert(0, "hello")
    assert "hello" == dll[0]
    assert 1 == dll[1]


def test_insert():
    dll = Dll(0)
    dll.append(1)
    dll.insert(1, "hello")
    assert 0 == dll[0]
    assert "hello" == dll[1]
    assert 1 == dll[2]


def test_insert_at_end():
    dll = Dll(0)
    dll.insert(1, 'hey')
    assert 0 == dll[0]
    assert "hey" == dll[1]


def test_insert_error():
    dll = Dll()
    with pytest.raises(IndexError):
        dll.insert(1, "hey")


def test_insert_error_2():
    dll = Dll(0)
    dll.append(1)
    with pytest.raises(IndexError):
        dll.insert(3, "hello")


def test_delete_head():
    dll = Dll(0)
    dll.delete(0)
    assert None is dll.head


def test_delete():
    dll = Dll(0)
    dll.append(1)
    dll.delete(1)
    assert None is dll.head.next


def test_delete_2():
    dll = Dll(0)
    dll.append(1)
    dll.append(2)
    dll.delete(1)
    assert 0 == dll[0]
    assert 2 == dll[1]
    assert 2 == dll.head.next.value
    assert 0 == dll.head.next.prev.value


def test_delete_3():
    dll = Dll(0)
    dll.append(1)
    dll.delete(0)
    assert 1 == dll[0]


def test_delete_error():
    dll = Dll()
    with pytest.raises(IndexError):
        dll.delete(0)


def test_delete_error_2():
    dll = Dll(1)
    dll.append(2)
    with pytest.raises(IndexError):
        dll.delete(2)
