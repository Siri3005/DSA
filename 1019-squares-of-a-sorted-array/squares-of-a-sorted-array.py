class Solution(object):
    def sortedSquares(self, nums):
        res=[]
        for num in nums:
            res.append(num**2)
        return sorted(res)
        