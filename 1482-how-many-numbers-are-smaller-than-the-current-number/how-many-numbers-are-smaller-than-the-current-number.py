class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        res=[0]*len(nums)
        for i in range(len(nums)):
            count=0
            for j in range(len(nums)):
                if i!=j:
                    if nums[j]<nums[i]:
                        count+=1
            res[i]=count
        return res

