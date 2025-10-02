class Solution(object):
    def jump(self, nums):
        jumps=0
        farthest=0
        cur_bound=0
        for i in range(len(nums)-1):
            farthest=max(farthest,i+nums[i])
            if i==cur_bound:
                jumps+=1
                cur_bound=farthest
        return jumps
        