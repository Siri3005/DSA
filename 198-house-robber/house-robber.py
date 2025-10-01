class Solution(object):
    def rob(self, nums):
        n=len(nums)+1
        dp=[0]*n
        dp[0]=0
        dp[1]=nums[0]
        for i in range(2,n):
            dp[i]=max(dp[i-1],nums[i-1]+dp[i-2])
        return max(dp[-1],dp[-2])
        