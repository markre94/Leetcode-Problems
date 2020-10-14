from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # s = s[::-1]
        for i in range((len(s)) //2):
            s [i], s [len(s)-1 - i] = s [len(s) -1 - i], s [i]
        print(s)


ob1 = Solution()
ob1.reverseString(["h","e","l","l","o"])


