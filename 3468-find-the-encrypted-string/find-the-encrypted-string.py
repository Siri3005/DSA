class Solution(object):
    def getEncryptedString(self, s, k):
        res=''
        for i in range(len(s)):
            res=res+s[(i+k)%len(s)]
        return res
        