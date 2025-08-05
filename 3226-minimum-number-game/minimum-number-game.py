class Solution(object):
    def numberGame(self, nums):
        arr=[]
        nums.sort(reverse=True)
        while nums:
            ele1=nums.pop()
            ele2=nums.pop()
            arr.append(ele2)
            arr.append(ele1)
        return arr

