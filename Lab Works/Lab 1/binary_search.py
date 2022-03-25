def binary_search(values, target):
    low = 0
    high = len(values) - 1
    while low <= high:
        mid = (low + high) // 2
        if values[mid] == target:
            return mid
        elif values[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1    