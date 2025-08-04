class Solution(object):
    def findMaxK(self, nums):
        res=0
        for num in nums:
            if num>0:
                if num*-1 in nums:
                    res=max(res,num)
        if res:
            return res
        else:
            return -1

        