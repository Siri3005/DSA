class Solution(object):
    def findTheDifference(self, s, t):
        '''s=list(s)
        for i in range(len(t)):
            if t[i] not in s:
                return t[i]
            s.remove(t[i])'''
        s=list(s)
        for i in range(len(t)):
            if t[i] not in s:
                return t[i]
            s.remove(t[i])
        