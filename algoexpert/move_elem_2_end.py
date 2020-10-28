def moveElementToEnd(array, toMove):
    # Write your code here.
    left = 0
    right = len(array) - 1

    while left < right:
        if array[left] == toMove and array[right] != toMove:
            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1
        elif array[left] == toMove and array[right] == toMove:
            right -= 1
        else:
            left += 1

    return array


print(moveElementToEnd([2, 1, 2, 2, 2, 3, 4, 2], 2))
