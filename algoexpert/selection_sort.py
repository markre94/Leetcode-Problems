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


def selectionSort(array):
    # Write your code here.
    i = 0
    while i < len(array):
        smallest = min(array)
        if array[i] <
        array[i], array[array.index(smallest)] = array[array.index(smallest)], array[i]
        i += 1
    return array





print(selectionSort([8, 5, 2, 9, 5, 6, 3]))
