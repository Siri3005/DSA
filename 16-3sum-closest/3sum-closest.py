class Solution(object):
    def threeSumClosest(self, nums, target):
        res=nums[0] + nums[1] + nums[2]
        nums.sort()
        for i in range(len(nums)):
            if i>0 and nums[i-1]==nums[i]:
                continue
            left=i+1
            right=len(nums)-1
            while left<right:
                total=nums[i]+nums[left]+nums[right]
                if abs(target-total)<abs(target-res):
                    res=total
                if total<target:
                    left+=1
                elif total>target:
                    right-=1
                else:
                    return total
        return res
                
                