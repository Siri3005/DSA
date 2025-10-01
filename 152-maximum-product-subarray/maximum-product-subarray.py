class Solution(object):
    def maxProduct(self, nums):
        if not nums:
            return 0
        max_product=ans=min_product=nums[0]
        for i in range(1,len(nums)):
            num=nums[i]
            if num<0:
                max_product,min_product=min_product,max_product
            max_product=max(num,max_product*num)
            min_product=min(num,min_product*num)
            ans=max(ans,max_product)
        return ans
        