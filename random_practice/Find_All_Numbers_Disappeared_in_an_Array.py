from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List [int]) -> List [int]:
        sorted_nums = sorted(nums)
        result =[]
        for i in range(1, max(sorted_nums)+1):
            if i not in sorted_nums:
                result.append(i)

        return result

