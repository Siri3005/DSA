class Solution(object):
    def dominantIndex(self, nums):
        maxi=max(nums)
        for num in nums:
            if num!=maxi and num*2>maxi:
                return -1
        return nums.index(maxi)