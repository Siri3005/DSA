from collections import defaultdict
class Solution(object):
    def topKFrequent(self, nums, k):
        hashmap=defaultdict(int)
        for num in nums:
            hashmap[num]+=1
        hashmap=sorted(hashmap.items(),key=lambda x:x[1],reverse=True)
        return [item[0] for item in hashmap[:k]]
        