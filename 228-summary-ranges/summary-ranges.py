class Solution(object):
    def summaryRanges(self, nums):
        if not nums:
            return []
        start=nums[0]
        res=[]
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]+1:
                if start==nums[i-1]:
                    res.append(str(start))
                else:
                    res.append(str(start) + "->" + str(nums[i-1]))
                start=nums[i]
        if start==nums[-1]:
            res.append(str(start))
        else:
            res.append(str(start)+'->'+str(nums[-1]))   
        return res