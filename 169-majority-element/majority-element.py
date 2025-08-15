class Solution(object):
    def majorityElement(self, nums):
        k=len(nums)//2
        from collections import defaultdict
        hashmap=defaultdict(int)
        for num in nums:
            hashmap[num]+=1
        maxim=0
        res=0
        for key,value in hashmap.items():
            if value>k and value>maxim:
                res=key
                maxim=value
        return res