def spiralTraverse(array):
    result = []
    start_row = 0
    end_row = len(array)
    start_col = 0
    end_col = len(array[0])

    while start_row <= end_row - 1 and start_col <= end_col - 1:
        # first row
        for i in range(start_col, end_col):
            result.append(array[start_row][i])

        # last column

        for i in range(start_row + 1, end_row):
            result.append(array[i][end_col - 1])

        # last row

        for i in range(end_col - 2, start_col - 1, -1):
            if start_col == end_col:
                break
            result.append(array[end_row - 1][i])

        # first column

        for i in range(end_row - 2, start_row, -1):
            if start_row == end_row:
                break
            result.append(array[i][start_col])

        start_col += 1
        start_row += 1
        end_row -= 1
        end_col -= 1

    return result


# print(spiralTraverse([[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]))
#
# print(spiralTraverse([
#     [27, 12, 35, 26],
#     [25, 21, 94, 11],
#     [19, 96, 43, 56],
#     [55, 36, 10, 18],
#     [96, 83, 31, 94],
#     [93, 11, 90, 16]
#   ]))

print(spiralTraverse([[1, 2, 3], [12, 13, 4], [11, 14, 5], [10, 15, 6], [9, 8, 7]]))
