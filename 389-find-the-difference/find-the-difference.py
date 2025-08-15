class Solution(object):
    def findTheDifference(self, s, t):
        hashmap1=defaultdict(int)
        hashmap2=defaultdict(int)
        for ch in s:
            hashmap1[ch]+=1
        for ch in t:
            hashmap2[ch]+=1
        for ch in t:
            if ch not in s or hashmap1[ch]<hashmap2[ch]:
                return ch