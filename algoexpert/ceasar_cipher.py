import string as st


def caesarCipherEncryptor(string, key):
    # Write your code here.
    result_str = ""
    alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    x = {}
    for i in range(len(alphabet)):
        x[alphabet[i]] = i

    for j in range(len(string)):

        new_idx = x[string[j]] + key

        if new_idx > 25:
            result_idx = 25 - new_idx
            result_str +=


print(caesarCipherEncryptor('zbc', 3))
