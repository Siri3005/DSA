class Solution(object):
    def countElements(self, nums):
        maxim=max(nums)
        minim=min(nums)
        count=0
        for num in nums:
            if num>minim and num<maxim:
                count+=1
        return count
        