class Solution(object):
    def findRelativeRanks(self, score):
        arr=score[:]
        score.sort(reverse=True)
        res=['']*len(score)
        for i,s in enumerate(score):
            idx=arr.index(s)
            if i==0:
                res[idx]='Gold Medal'
            elif i==1:
                res[idx]='Silver Medal'
            elif i==2:
                res[idx]='Bronze Medal'
            else:
                res[idx]=str(i+1)
        return res
