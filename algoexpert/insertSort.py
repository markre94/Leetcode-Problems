def insertionSort(array):
    for i in range(1, len(array)):
        curr_idx = i
        j = i - 1
        while j >= 0 and array[curr_idx] < array[j]:
            swap(curr_idx, j, array)
            j -= 1
            curr_idx -= 1


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]


print(insertionSort([3, 2, 1, 4, 6, 7, 10]))
