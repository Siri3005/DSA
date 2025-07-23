class Solution(object):
    def findDisappearedNumbers(self, nums):
        list1=set(range(1,len(nums)+1))
        return list(list1-set(nums))