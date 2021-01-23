def firstDuplicateValue(array):
    # Write your code here.
    dic = {}
    for i in range(len(array)):
        if array[i] not in dic:
            dic[array[i]] = 1
        else:
            return array[i]


array = [2, 1, 5, 2, 3, 3, 4]
print(firstDuplicateValue(array))
