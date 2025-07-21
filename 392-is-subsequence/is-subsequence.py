class Solution(object):
    def isSubsequence(self, s, t):
        res=''
        idx=0
        for i in range(len(t)):
            if idx<len(s) and t[i]==s[idx]:
                res+=t[i]
                idx+=1
        return res==s
            
        