class Solution(object):
    def pivotIndex(self, nums):
        for i in range(len(nums)):
            if i==0:
                if sum(nums[1:])==0:
                    return i
            elif i==len(nums)-1:
                if sum(nums[:len(nums)-1])==0:
                    return i
            else:
                if sum(nums[0:i])==sum(nums[i+1:]):
                    return i
        return -1
