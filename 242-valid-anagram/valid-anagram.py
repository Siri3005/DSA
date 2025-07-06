class Solution(object):
    def isAnagram(self, s, t):
        if len(s)==len(t):
            if sorted(list(s))==sorted(list(t)):
                return True
        return False
        