class Solution(object):
    def specialArray(self, nums):
        for i in range(1,len(nums)+1):
            count=0
            for j in range(len(nums)):
                if nums[j]>=i:
                    count+=1
            if count==i:
                return count
        return -1
        