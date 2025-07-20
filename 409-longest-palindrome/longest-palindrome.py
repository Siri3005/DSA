class Solution(object):
    def longestPalindrome(self, s):
        if len(s)==1:
            return 1
        hashmap={}
        for i in range(len(s)):
            hashmap[s[i]]=0
        for i in range(len(s)):
            hashmap[s[i]]+=1
        res=0
        values=list(hashmap.values())
        values.sort(reverse=True)
        odd_values=[]
        has_odd=False
        for i in range(len(values)):
            if values[i]%2==0:
                res+=values[i]
            else:
                res+=values[i]-1
                has_odd=True
        if has_odd:
            res+=1
        return res

        