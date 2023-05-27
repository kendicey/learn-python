def binary_search(list, target):
    first = 0
    last = len(list) - 1

    while first <= last:
        midpoint = (first + last) // 2   # round to integer

        if list[midpoint] == target:     # if midpoint is the target
            return midpoint
        elif list[midpoint] < target:    # if midpoint is less than the target
            first = midpoint + 1
        else:
            last = midpoint - 1          # if midpoint is greater than the target

    return None


def verify(index):
    if index is not None:
        print("Target found at index: ", index)
    else:
        print("Target not in list")


# list has to be sorted for binary search
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = binary_search(numbers, 12)
verify(result)

result = binary_search(numbers, 6)
verify(result)
