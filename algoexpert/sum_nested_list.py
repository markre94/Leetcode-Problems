from typing import List


def productSum(array, multiplier=1):
    # Write your code here.
    result_sum = 0
    for elem in array:
        if isinstance(elem, List):
            result_sum += productSum(elem, multiplier + 1)
        else:
            result_sum += elem

    return multiplier * result_sum


print(productSum([5, 2, [7, -1], 3, [6, [-13, 8], 4]]))
