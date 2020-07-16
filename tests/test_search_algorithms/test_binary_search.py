import pytest
from my_python_algorithms.search_algorithms.binary_search import *


def test_empty_list():
    assert -1 == binary_search_iterative([], 1)


def test_single_value_not_in_list():
    assert -1 == binary_search_iterative([0], 1)


def test_value_lower_than_list():
    assert -1 == binary_search_iterative([1, 2, 3, 4, 5], -1)


def test_intermediate_value():
    assert -1 == binary_search_iterative([1, 2, 3], 2.5)


def test_value_higher_than_list():
    assert -1 == binary_search_iterative([1, 2, 3], 5)


def test_single_value_in_list():
    assert 0 == binary_search_iterative([1], 1)


def test_value_in_list_1():
    assert 2 == binary_search_iterative([-5, -3, 0, 1], 0)


def test_value_in_list_2():
    assert 0 == binary_search_iterative([-100, 1, 2, 3], -100)


def test_value_in_list_3():
    assert 5 == binary_search_iterative([-5, 1, 2, 4, 6, 10], 10)


def test_empty_list_rec():
    assert -1 == binary_search_recursive([], 1)


def test_single_value_not_in_list_rec():
    assert -1 == binary_search_recursive([0], 1)


def test_value_lower_than_list_rec():
    assert -1 == binary_search_recursive([1, 2, 3, 4, 5], -1)


def test_intermediate_value_rec():
    assert -1 == binary_search_recursive([1, 2, 3], 2.5)


def test_value_higher_than_list_rec():
    assert -1 == binary_search_recursive([1, 2, 3], 5)


def test_single_value_in_list_rec():
    assert 0 == binary_search_recursive([1], 1)


def test_value_in_list_1_rec():
    assert 2 == binary_search_recursive([-5, -3, 0, 1], 0)


def test_value_in_list_2_rec():
    assert 0 == binary_search_recursive([-100, 1, 2, 3], -100)


def test_value_in_list_3_rec():
    assert 5 == binary_search_recursive([-5, 1, 2, 4, 6, 10], 10)
