from typing import List
from itertools import permutations


class Solution:
    def largestTimeFromDigits(self, A: List [int]) -> str:
        p = list(permutations(sorted(A, reverse=True)))
        for h1,h2,m1,m2 in p:
            hour = h1 * 10 + h2
            minute = m1 * 10 + m2

            if hour < 24 and minute < 60:
                return f"{h1}{h2}:{m1}{m2}"





class Solution1:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if len(nums) == 0 and k <= 0:
            return False
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if abs(nums[i] - nums[j]) <= t and abs(i - j) <= k:
                    return True
        return False


ob2=Solution1()
print(ob2.containsNearbyAlmostDuplicate([1,5,9,1,5,9],2,3))











ob = Solution()
print(ob.largestTimeFromDigits(A=[1,2,3,4]))