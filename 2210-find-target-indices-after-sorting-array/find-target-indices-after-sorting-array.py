class Solution(object):
    def targetIndices(self, nums, target):
        nums.sort()
        if target not in nums:
            return []
        n=nums.count(target)
        idx=nums.index(target)
        return range(idx,idx+n)