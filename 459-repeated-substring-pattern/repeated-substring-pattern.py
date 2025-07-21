class Solution(object):
    def repeatedSubstringPattern(self, s):
        subs=''
        for i in range(len(s)-1):
            subs+=s[i]
            if subs*(len(s)//len(subs))==s:
                return True
        return False