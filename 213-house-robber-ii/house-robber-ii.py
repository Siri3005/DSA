class Solution(object):
    def rob(self, nums):
        def cal_mon(nums):
            n=len(nums)
            dp=[0]*(n+1)
            dp[0]=0
            dp[1]=nums[0]
            n=len(nums)
            for i in range(2,n+1):
                dp[i]=max(dp[i-1],nums[i-1]+dp[i-2])
            return max(dp[-1],dp[-2])
        if len(nums)==1:
            return nums[0]
        dp1=cal_mon(nums[:-1])
        dp2=cal_mon(nums[1:])
        return max(dp1,dp2)