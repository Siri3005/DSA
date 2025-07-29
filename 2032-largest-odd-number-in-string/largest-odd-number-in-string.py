class Solution(object):
    def largestOddNumber(self, num):
        for i in range(len(num),0,-1):
            if int(num[i-1])%2==1:
                return num[:i]
        return ""