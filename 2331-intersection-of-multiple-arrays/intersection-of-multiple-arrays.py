class Solution(object):
    def intersection(self, nums):
        if len(nums)==1:
            return sorted(nums[0])
        pre=set(nums[0])
        res=[]
        for i in range(1,len(nums)):
            curr=set(nums[i])
            res=list(pre & curr)
            pre=set(res)
        return sorted(res)