class Solution(object):
    def majorityElement(self, nums):
        from collections import defaultdict
        hashmap=defaultdict(int)
        for num in nums:
            hashmap[num]+=1
        k=len(nums)//3
        res=[]
        for key,value in hashmap.items():
            if value>k:
                res.append(key)

        return res