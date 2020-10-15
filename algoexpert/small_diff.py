def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
    """Not efficent enough"""

    arr_one = sorted(arrayOne)
    arr_two = sorted(arrayTwo)
    diff = float("inf")
    num_1 = float("inf")
    num_2 = float("inf")
    for i in range(len(arr_one)):
        for j in range(len(arr_two)):
            sub_diff = abs(arr_one[i] - arr_two[j])
            if sub_diff < diff:
                diff = sub_diff
                num_1, num_2 = arr_one[i], arr_two[j]
    return [num_1, num_2]


if __name__ == "__main__":
    print(smallestDifference([-1, 5, 10, 20, 28, 3],[26, 134, 135, 15, 17]))