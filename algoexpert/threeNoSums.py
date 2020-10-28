""" First solution not very efficent
O(n^3) time."""


def threeNumberSum1(array, targetSum):
    # Write your code here.
    array.sort()
    result = []
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            for z in range(j + 1, len(array)):
                if abs(array[i] + array[j] + array[z]) == targetSum:
                    result.append([array[i], array[j], array[z]])
    return result if result else []


print(threeNumberSum1([12, 3, 1, 2, -6, 5, -8, 6], 0))

"""effective solution"""


def threeNumberSum(array, targetSum):
    # Write your code here.
    array.sort()
    result_arr = []
    # left = 1
    # right = len
    for i in range(len(array)-1):
        left = i + 1
        right = len(array) - 1

        while left < right:
            temp_sum = array[i] + array[left] + array[right]
            if temp_sum > targetSum:
                right -= 1
            elif temp_sum < targetSum:
                left += 1
            elif temp_sum == targetSum:
                result_arr.append([array[i], array[left], array[right]])
                left += 1
                right -= 1

    return result_arr if result_arr else []


print(threeNumberSum([12, 3, 1, 2, -6, 5, -8, 6], 0))
