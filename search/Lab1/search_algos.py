def linear_search(values, target):
    '''Linear search algorithm'''
    for i, value in enumerate(values):
        if value == target:
            return i
    return -1

def binary_search(values, target, low, high):
    '''Binary search algorithm'''
    mid = (high+low-1)//2
    if high - low <= 0:
        return -1
    
    if target > values[mid]:
        low = mid + 1
        return binary_search(values, target, low, high)
    elif target < values[mid]:
        high = mid
        return binary_search(values, target, low, high)
    else:
        return mid
     