class Solution(object):
    def findShortestSubArray(self, nums):
        from collections import defaultdict
        count=defaultdict(int)
        firstidx={}
        lastidx={}
        for i,num in enumerate(nums):
            count[num]+=1
            if num not in firstidx:
                firstidx[num]=i
            lastidx[num]=i
        degree=max(count.values())
        min_length=float('inf')
        for num in count:
            if count[num]==degree:
                length=lastidx[num]-firstidx[num]+1
                min_length=min(min_length,length)
        return min_length
        
        