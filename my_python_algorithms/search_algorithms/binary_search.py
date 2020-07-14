def binary_search(array, value) -> int:
    """Return index of the value in the array, or -1 if value is not found."""
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
