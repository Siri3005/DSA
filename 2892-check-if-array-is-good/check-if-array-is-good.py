class Solution(object):
    def isGood(self, nums):
        max_ele=max(nums)
        if len(nums)!=(max_ele+1):
            return False
        nums.sort()
        for i in range(1,max_ele):
            if nums[i-1]!=i:
                return False
        if nums[-1]!=max_ele or nums[-2]!=max_ele:
            return False
        return True
        