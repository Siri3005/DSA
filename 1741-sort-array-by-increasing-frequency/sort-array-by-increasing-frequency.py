class Solution(object):
    def frequencySort(self, nums):
        from collections import defaultdict
        hashmap=defaultdict(int)
        for num in nums:
            hashmap[num]+=1
        nums.sort(key=lambda x:(hashmap[x],-x))
        return nums
            