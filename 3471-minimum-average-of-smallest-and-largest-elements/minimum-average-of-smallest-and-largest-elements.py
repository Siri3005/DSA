class Solution(object):
    def minimumAverage(self, nums):
        count=0
        n=len(nums)
        averages=[]
        while count<=(n/2) and nums:
            avg=(float(min(nums)+float(max(nums)))/2)
            averages.append(avg)
            nums.remove(min(nums))
            nums.remove(max(nums))
            count+=1
        return float(min(averages))