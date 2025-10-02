class Solution(object):
    def uniquePaths(self, m, n):
        dp=[[0]*n for _ in range(m)]
        dp[0][0]=1
        for i in range(1,n):
            dp[0][i]=1
        for j in range(1,m):
            dp[j][0]=1
        for r in range(1,m):
            for c in range(1,n):
                dp[r][c]=dp[r-1][c]+dp[r][c-1]
        return dp[-1][-1]

        