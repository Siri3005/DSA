class Solution(object):
    def searchInsert(self, nums, target):
        if target>max(nums):
            return len(nums)
        if target in nums:
            return nums.index(target)
        if target<min(nums):
            return 0
        for i in range(len(nums)):
            if target>nums[i] and target<nums[i+1]:
                return i+1