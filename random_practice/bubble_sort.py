import random
def buble_sort(list_in):
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i in range(len(list_in) - 1):
            if list_in[i] > list_in[i+1]:
                is_sorted = False
                list_in[i], list_in[i+1] = list_in[i+1], list_in[i]
        return list_in






