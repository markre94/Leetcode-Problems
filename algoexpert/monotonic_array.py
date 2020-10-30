def isMonotonic(array):
    result = []
    for i in range(1, len(array)):
        result.append(get_direction(array[i-1], array[i]))
    if "inc" in set(result) and "dec" in set(result):
        return False
    else:
        return True


def get_direction(x1, x2):
    if x1 < x2:
        return "inc"
    elif x1 > x2:
        return "dec"
    else:
        return "eq"


print(isMonotonic([-1, -5, -10, -1100, -1100, 250, -1102, -9001]))
print(isMonotonic([1, 5, 10, 1100, 1101, 1102, 9001]))
