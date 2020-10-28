""" First solution not very efficent
O(n^3) time."""


def threeNumberSum(array, targetSum):
    # Write your code here.
    array.sort()
    result = []
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            for z in range(j + 1, len(array)):
                if abs(array[i] + array[j] + array[z]) == targetSum:
                    result.append([array[i], array[j], array[z]])
    return result if result else []


print(threeNumberSum([12, 3, 1, 2, -6, 5, -8, 6], 0))
