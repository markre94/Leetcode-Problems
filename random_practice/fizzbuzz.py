# # Unikć pisania takich samych warunkow dwa razy np
#
# # if i%3==0
# # if i%3==0  and if i%5==0
#
# def play_fizz_buzz():
#     for i in range(1, 100):
#         output = ''
#
#         if i % 3 == 0:
#             output += 'Open'
#         if i % 7 == 0:
#             output += 'Source'
#
#         if output == '':
#             print(i)
#         else:
#             print(output)
#
#
# # print(play_fizz_buzz())
#
#
# def get_digit(list_in: str):
#     return sum([int(elem) for elem in list_in if elem.isdigit()])
#
#
# def get_digit_recursive(list_in: str):
#      if not list_in:
#          return 0
#
#      if list_in[0].isdigit():
#          value = int(list_in[0])
#          return value + get_digit_recursive(list_in [1:])
#      else:
#          return 0 + get_digit_recursive(list_in[1:])
#
#
#
#
# print(get_digit('1234dasd039823'))
# print(get_digit_recursive('1234dasd039823'))
# # assert get_digit('1234dasd039823') == ['1', '2', '3', '4', '0', '3', '9', '8', '2', '3']
# import requests, re
# # get contents of the page
# r = requests.get('http://www.sap.com/belgique/index.html')
# #Create a regular expression to find all SAP elements
# regex = re.compile(r'SAP')
# if regex:
#     new_page_content = re.sub('SAP', 'Odoo', r.text)
#     print(new_page_content)
#
#     #Saved changed content of the page
#     text_file = open("sample.html", "w")
#     n = text_file.write(new_page_content)
#     text_file.close()

# import random
#
#
# class Game:
#     def __init__(self):
#         self.secret = random.randint(1, 1000000)
#
#     def verify(self, number: int) -> int:
#         if number == self.secret:
#             return 0
#         elif number > self.secret:
#             return -1
#         else:
#             return 1
#
#     def play_game(self):
#         low = 1
#         high = 1000000
#         tries = 0
#         while low <= high and tries < 50:
#             mid = (low + high) // 2
#             guess = self.verify(mid)
#             if guess == 0:
#                 return f'You guessed the number {mid} in {tries}'
#             if guess == -1:
#                 tries += 1
#                 high = mid - 1
#             if guess == 1:
#                 tries += 1
#                 low = mid + 1
#         return f'You lost!'
#
#
# if __name__ == "__main__":
#     game = Game()
#     print(game.secret)
#     print(game.play_game())
#
# def delete_nth_byte(n: int):
#     with open("filename", "wb") as f:
#         bytes_read = f.read()
#     for b in range(len(bytes_read)):
#         if b % n == 0:
#             del b
import string
from collections import Counter
from typing import List


class Solution:
    def titleToNumber(self, s: str) -> int:
        # alpha = (string.ascii_uppercase)
        num = 0
        for i,char in enumerate(s[::-1]):
            # pos = alpha.index(char) + 1
            val = ord(char) - 64
            num += val * (26 ** i)


        return num


ob = Solution()
print(ob.titleToNumber('ZY'))


class Solutionx:
    def smallerNumbersThanCurrent(self, nums: List [int]) -> List [int]:
        result = []
        elems = sorted(nums)
        added = {}
        count = 0
        for i in range(len(nums)):
            if elems[i] not in added:
                added[elems[i]] = count
                count += 1
            else:
                count += 1

        for i in range(len(nums)):
            nums[i] = added[nums[i]]

        return nums







ob1 = Solutionx()
print(ob1.smallerNumbersThanCurrent([8,1,2,2,3]))


class Solutionz:
    def reverse(self, x: int) -> int:
        limit = 2147483648
        num_str = str(x)
        if x > 0:
            if int(num_str [::-1]) < limit:
                return int(num_str[::-1])
            else:
                return 0
        if x < 0:
            num_str = str(x)[1:]
            if int(num_str [::-1]) < limit:
                return -int(num_str [::-1])
            else:
                return 0



obx = Solutionz()
print(obx.reverse(123))
print(obx.reverse(-321))

print(obx.reverse(-1534236469))
print(obx.reverse(1563847412))


