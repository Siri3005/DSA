class Solution(object):
    def containsDuplicate(self, nums):
        from collections import defaultdict
        hashmap=defaultdict(int)
        for num in nums:
            hashmap[num]+=1
            if hashmap[num]>1:
                return True
        return False
        