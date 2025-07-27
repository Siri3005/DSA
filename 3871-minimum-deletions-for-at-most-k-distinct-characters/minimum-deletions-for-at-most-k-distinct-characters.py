class Solution(object):
    def minDeletion(self, s, k):
        from collections import defaultdict
        hashmap=defaultdict(int)
        for ch in s:
            hashmap[ch]+=1
        d=len(hashmap)
        if d<=k:
            return 0
        freqs=sorted(hashmap.values())
        to_rem=d-k
        deletions=sum(freqs[:to_rem])
        return deletions
        
        