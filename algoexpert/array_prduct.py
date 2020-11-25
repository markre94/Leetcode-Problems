def arrayOfProducts(array):
    # Write your code here.
    prod_array = []
    for i in range(len(array)):
        left = i - 1
        right = i + 1
        product_l = 1
        product_r = 1
        while left >= 0:
            product_l *= array[left]
            left -= 1
        while right < len(array):
            product_r *= array[right]
            right += 1
        prod_array.append(product_r * product_l)

    return prod_array


print(arrayOfProducts([5, 1, 4, 2]))
