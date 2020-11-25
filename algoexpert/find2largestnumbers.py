def findThreeLargestNumbers(array):
    # Write your code here.
    three_maxes = []
    i = 1
    while i <= 3:
        m_value = max(array)
        array.pop(array.index(m_value))
        three_maxes.append(m_value)
        i += 1
    return sorted(three_maxes)


print(findThreeLargestNumbers([141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]))


def findThreeLargestNumbers2(array):
    # Write your code here.
    three_maxes = [None, None, None]

    for i in range(len(array)):

        if three_maxes[2] is None or array[i] > three_maxes[2]:
            for j in range(3):
                if j == 2:
                    three_maxes[j] = array[i]
                else:
                    three_maxes[j] = three_maxes[j + 1]

        elif three_maxes[1] is None or array[i] > three_maxes[1]:
            for j in range(2):
                if j == 1:
                    three_maxes[j] = array[i]
                else:
                    three_maxes[j] = three_maxes[j + 1]
        elif three_maxes[0] is None or array[i] > three_maxes[0]:
            for j in range(1):
                if j == 0:
                    three_maxes[j] = array[i]
                else:
                    three_maxes[j] = three_maxes[j + 1]

    return three_maxes


print(findThreeLargestNumbers2([141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]))
print(findThreeLargestNumbers2([141, 1, 17]))
