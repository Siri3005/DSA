class Solution(object):
    def longestConsecutive(self, nums):
        if not nums:
            return 0
        sorted_arr=sorted(set(nums))
        max_count=1
        count=1
        for i in range(1,len(sorted_arr)):
            if sorted_arr[i]-sorted_arr[i-1]==1:
                count+=1
                max_count=max(count,max_count)
            else:
                count=1
        return max_count
