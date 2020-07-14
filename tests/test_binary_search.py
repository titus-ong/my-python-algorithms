import pytest
from my_python_algorithms.search_algorithms.binary_search import binary_search


def test_empty_list():
    assert -1 == binary_search([], 1)


def test_single_value_not_in_list():
    assert -1 == binary_search([0], 1)


def test_value_lower_than_list():
    assert -1 == binary_search([1, 2, 3, 4, 5], -1)


def test_intermediate_value():
    assert -1 == binary_search([1, 2, 3], 2.5)


def test_value_higher_than_list():
    assert -1 == binary_search([1, 2, 3], 5)


def test_single_value_in_list():
    assert 0 == binary_search([1], 1)


def test_value_in_list_1():
    assert 2 == binary_search([-5, -3, 0, 1], 0)


def test_value_in_list_2():
    assert 0 == binary_search([-100, 1, 2, 3], -100)


def test_value_in_list_3():
    assert 5 == binary_search([-5, 1, 2, 4, 6, 10], 10)
