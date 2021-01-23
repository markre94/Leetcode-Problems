def spiralTraverse(array):
    result = []
    start_row = 0
    end_row = len(array) - 1
    start_col = 0
    end_col = len(array[0]) - 1

    while start_row <= end_row and start_col <= end_col:
        # first row
        for i in range(start_col, end_col + 1):
            result.append(array[start_row][i])

        # last column

        for i in range(start_row + 1, end_row + 1):
            result.append(array[i][end_col])

        # last row

        for i in range(end_col - 1, start_col - 1, -1):
            if start_row == end_row:
                break
            result.append(array[end_row][i])

        # first column

        for i in range(end_row - 1, start_row, -1):
            if start_col == end_col:
                break
            result.append(array[i][start_col])

        start_col += 1
        start_row += 1
        end_row -= 1
        end_col -= 1

    return result


print(spiralTraverse([[1, 2, 3], [12, 13, 4], [11, 14, 5], [10, 15, 6], [9, 8, 7]]))
