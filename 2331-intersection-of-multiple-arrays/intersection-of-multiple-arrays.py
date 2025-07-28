class Solution(object):
    def intersection(self, nums):
        res=set(nums[0])
        for i in range(1,len(nums)):
            curr=set(nums[i])
            res=res & curr
        return sorted(list(res))