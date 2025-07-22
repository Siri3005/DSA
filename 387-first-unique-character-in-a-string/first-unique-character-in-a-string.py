class Solution(object):
    def firstUniqChar(self, s):
        hashmap={}
        for ch in s:
            hashmap[ch]=0
        for ch in s:
            hashmap[ch]+=1
        for i in range(len(s)):
            if hashmap[s[i]]==1:
                return i
        return -1