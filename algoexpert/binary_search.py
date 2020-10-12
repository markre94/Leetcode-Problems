def binarySearch(array, target):
    # Write your code here.
    low = 0
    high = len(array) - 1
    while low < high:
        mid = (high + low)
        guess = array [mid]

        if guess == target:
            return mid
        if guess > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1


print(binarySearch([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 33))