class Solution(object):
    def rob(self, nums):
        n=len(nums)+1
        dp=[0]*n
        dp[0]=0
        dp[1]=nums[0]
        for i in range(2,n):
            for j in range(i-1):
                dp[i]=max(dp[i],nums[i-1]+dp[j])
        return max(dp[-1],dp[-2])
        