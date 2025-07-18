class Solution(object):
    def firstUniqChar(self, s):
        hashmap={}
        for i in range(len(s)):
            hashmap[s[i]]=0
        for char in s:
            hashmap[char]+=1
        for i in range(len(s)):
            if hashmap[s[i]]==1:
                return i
        return -1
        