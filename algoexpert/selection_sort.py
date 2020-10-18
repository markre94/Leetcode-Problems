# def selectionSort_1(array):
#     # Write your code here.
#     result_array = []
#
#     for i in range(len(array)):
#         smallest = min(array)
#         result_array.append(array.pop(array.index(smallest)))
#
#     return result_array
#
#
# print(selectionSort_1(array=[8, 5, 2, 9, 5, 6, 3]))

# Second version with O(0) space complexity

def selectionSort(array):
    # Write your code here.
    for i in range(len(array)):
        smallestIdx = i
        for j in range(i + 1, len(array)):
            if array[j] < array[smallestIdx]:
                smallestIdx = j
        array[i], array[smallestIdx] = array[smallestIdx], array[i]

    return array


print(selectionSort([8, 5, 2, 9, 5, 6, 3]))
