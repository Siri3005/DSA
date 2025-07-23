class Solution(object):
    def findErrorNums(self, nums):
        n=len(nums)
        actual_sum=sum(set(nums))
        correct_sum=n*(n+1)//2
        duplicate=sum(nums)-actual_sum
        missing=correct_sum-actual_sum
        return [duplicate,missing]