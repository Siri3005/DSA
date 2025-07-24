class Solution(object):
    def findLucky(self, arr):
        from collections import defaultdict
        hashmap=defaultdict(int)
        res=-1
        for num in arr:
            hashmap[num]+=1
        for key,value in hashmap.items():
            if key==value:
                res=key
        return res