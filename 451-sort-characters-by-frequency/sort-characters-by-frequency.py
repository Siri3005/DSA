class Solution(object):
    def frequencySort(self, s):
        from collections import defaultdict
        hashmap=defaultdict(int)
        for char in s:
            hashmap[char]+=1
        s=list(s)
        hashmap=sorted(hashmap.items(),key=lambda item:item[1],reverse=True)
        res=''
        for key,val in hashmap:
            res+=key*val
        return res
