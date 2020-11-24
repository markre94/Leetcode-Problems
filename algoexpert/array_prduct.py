def arrayOfProducts(array):
    # Write your code here.
    for i in range(len(array)):
        product = 1
        for j in range(i + 1, len(array)):
            product *= array[j]
        array[i] = product
    return array


print(arrayOfProducts([5, 1, 4, 2]))
