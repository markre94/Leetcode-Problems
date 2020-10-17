def bubbleSort(array):
    # Write your code here.
    isSorted = False
    while not isSorted:
        isSorted = True
        for i in range(1, len(array)):
            if array[i] < array[i - 1]:
                array[i], array[i - 1] = array[i - 1], array[i]
                isSorted = False

    return array


print(bubbleSort(array=[3, 2, 5, 6, 1, 7]))
