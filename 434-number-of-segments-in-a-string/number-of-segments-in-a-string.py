class Solution(object):
    def countSegments(self, s):
        if not s:
            return 0
        res=s.split()
        return len(res)
        