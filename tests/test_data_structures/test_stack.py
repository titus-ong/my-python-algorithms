import pytest
from my_python_algorithms.data_structures.stack import Stack, EmptyStackException


def test_peek():
    s = Stack(1)
    assert 1 == s.peek()


def test_peek_error():
    s = Stack()
    with pytest.raises(EmptyStackException):
        s.peek()


def test_push():
    s = Stack()
    s.push(1)
    assert 1 == s.peek()


def test_push_2():
    s = Stack(1)
    s.push(2)
    assert 2 == s.peek()


def test_push_3():
    s = Stack(1)
    s.push(2)
    s.push(3)
    assert 3 == s.peek()


def test_pop():
    s = Stack(1)
    assert 1 == s.pop()


def test_pop_error():
    s = Stack()
    with pytest.raises(EmptyStackException):
        s.pop()


def test_pop_error_2():
    s = Stack(1)
    s.pop()
    with pytest.raises(EmptyStackException):
        s.pop()


def test_push_pop():
    s = Stack(1)
    s.push(2)
    s.pop()
    assert 1 == s.peek()
