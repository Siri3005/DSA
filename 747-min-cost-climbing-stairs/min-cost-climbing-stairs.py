class Solution(object):
    def minCostClimbingStairs(self, cost):
        n=len(cost)+1
        dp=[0]*n
        dp[0]=cost[0]
        dp[1]=cost[1]
        cost.append(0)
        for i in range(2,n):
            dp[i]=min(cost[i]+dp[i-1],cost[i]+dp[i-2])
        return dp[-1]

        