class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if len(s)==0:
            return 0
        max_len=0
        sub=''
        for c in s:
            if c in sub:
                index=sub.index(c)
                sub=sub[index+1:]
            sub+=c
            max_len=max(len(sub),max_len)
        return max_len