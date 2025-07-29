class Solution(object):
    def findLHS(self, nums):
        from collections import defaultdict
        max_len=0
        freq=defaultdict(int)
        for num in nums:
            freq[num]+=1
        for key in freq:
            if (key+1) in freq:
                length=freq[key]+freq[key+1]
                max_len=max(max_len,length)
        return max_len
        