def binarySearch(array, target):
    # Write your code here.
    low = 0
    high = len(array) - 1
    while low < high:
        mid = (high + low)
        guess = array [mid]

        if guess == target:
            return mid
        if guess > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1


print(binarySearch([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 33))


class Solution(object):
    def isUnivalTree(self, root):
        left_correct = (not root.left or root.val == root.left.val
                and self.isUnivalTree(root.left))
        right_correct = (not root.right or root.val == root.right.val
                and self.isUnivalTree(root.right))
        return left_correct and right_correct