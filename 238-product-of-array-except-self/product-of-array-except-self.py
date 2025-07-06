class Solution(object):
    def productExceptSelf(self, nums):
        prefix=[1]*len(nums)
        postfix=[1]*len(nums)
        pre_product=1
        for i in range(1,len(nums)):
            pre_product*=nums[i-1]
            prefix[i]=pre_product

        post_product=1
        for j in range(len(nums)-2,-1,-1):
            post_product*=nums[j+1]
            postfix[j]=post_product

        result=[0]*len(nums)
        for i in range(len(nums)):
            result[i]=prefix[i]*postfix[i]
        return result

        