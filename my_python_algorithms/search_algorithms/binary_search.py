"""
Binary search algorithm.
Return index of the value in the array, or -1 if value is not found.

Time complexity: O(log(n)) - search space is halved after each iteration

Space complexity: O(1)
"""


def binary_search_iterative(array, value) -> int:
    """Use moving pointers to size the array at each iteration."""
    left = 0
    right = len(array)
    while left < right:
        mid = (right - left) // 2 + left  # take lower mid
        if array[mid] == value:
            return mid
        if array[mid] > value:
            right = mid
        if array[mid] < value:
            left = mid+1
    return -1


def binary_search_recursive(array, value) -> int:
    """Recursively search the half of the array that may contain the value."""
    def recursive(array, left, right, value):
        if not array[left:right]:
            return -1
        mid = (right - left)//2 + left  # take lower mid
        if array[mid] == value:
            return mid
        if array[mid] > value:
            return recursive(array, left, mid, value)
        if array[mid] < value:
            return recursive(array, mid+1, right, value)

    right = len(array)
    return recursive(array, 0, right, value)
