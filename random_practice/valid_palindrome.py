# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         alpha_str = ''
#         for char in s:
#             if char.isalpha()  or char.isdigit():
#                 alpha_str += char
#         return alpha_str.upper() == alpha_str[::-1].upper()

def string_times(str, n):
    return str*n

print(string_times("Hi", 5))