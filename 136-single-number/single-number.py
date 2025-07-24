class Solution(object):
    def singleNumber(self, nums):
        from collections import defaultdict
        hashmap=defaultdict(int)
        for num in nums:
            hashmap[num]+=1
        for key,val in hashmap.items():
            if val==1:
                return key
        