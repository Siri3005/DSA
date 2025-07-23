class Solution(object):
    def arrayPairSum(self, nums):
        nums=sorted(nums)
        summ=0
        for i in range(0,len(nums),2):
            summ+=nums[i]
        return summ
        