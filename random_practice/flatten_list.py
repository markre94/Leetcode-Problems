from typing import List


def flatten_list(array: List):
    output_array = []
    for elem in array:
        if isinstance(elem, list):
            output_array.extend(flatten_list(elem))
        else:
            output_array.append(elem)
    return output_array


print(flatten_list([5, 2, [7, -1], 3, [6, [-13, 8], 4]]))
