from Find_All_Numbers_Disappeared_in_an_Array import Solution

def test_find_all():
    ob1 = Solution()

    assert ob1.findDisappearedNumbers([2,3,5]) == [1,4]
    assert ob1.findDisappearedNumbers([2,3,3,3,5,6,9]) == [1,4,7,8]
    assert  ob1.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]) == [5, 6]