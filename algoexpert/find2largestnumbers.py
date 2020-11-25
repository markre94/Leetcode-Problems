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
