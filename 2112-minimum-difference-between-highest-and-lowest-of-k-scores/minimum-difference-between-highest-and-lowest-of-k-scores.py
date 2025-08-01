class Solution(object):
    def minimumDifference(self, nums, k):
        if len(nums)==1:
            return 0
        nums.sort()
        mini=float('inf')
        for i in range(len(nums)-k+1):
            diff=nums[i+k-1]-nums[i]
            mini=min(diff,mini)
        return mini

                