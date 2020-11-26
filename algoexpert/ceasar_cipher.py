import string as st


def caesarCipherEncryptor(string, key):
    # Write your code here.
    result_str = ""
    alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]

    for i in range(len(string)):
        idx = alphabet.index(string[i]) + key
        if idx > 25:
            new_idx = idx - 26
            result_str += alphabet[new_idx]
        else:
            result_str += alphabet[idx]

    return result_str


print(caesarCipherEncryptor('xyz', 2))
