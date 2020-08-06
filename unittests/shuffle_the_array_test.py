from shuffle_the_array import Solution
import pytest

def test_solution():
    ob1 = Solution()
    # ob1.shuffle([1,2,3,4])
    assert ob1.shuffle([1, 2, 3, 4], 2) == [1, 3, 2, 4]
    assert ob1.shuffle(nums = [1,2,3,4,4,3,2,1], n = 4) == [1,4,2,3,3,2,4,1]

