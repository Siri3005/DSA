class Solution(object):
    def combinationSum(self, candidates, target):
        dp=[[] for _ in range(target+1)]
        dp[0]=[[]]
        dp[1]=[]
        for cand in candidates:
            for t in range(cand,target+1):
                for comb in dp[t-cand]:
                    dp[t].append(comb+[cand])
        return dp[target]

        