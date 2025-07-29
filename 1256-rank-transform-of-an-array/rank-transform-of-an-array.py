class Solution(object):
    def arrayRankTransform(self, arr):
        sorted_arr=sorted(set(arr))
        hashmap={}
        for i in range(len(sorted_arr)):
            hashmap[sorted_arr[i]]=i+1
        ranks=[]
        for num in arr:
            ranks.append(hashmap[num])
        return ranks