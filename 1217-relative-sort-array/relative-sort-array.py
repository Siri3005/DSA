class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        from collections import defaultdict
        hashmap=defaultdict(int)
        for i in range(len(arr1)):
            hashmap[arr1[i]]+=1
        res=[]
        for ele in arr2:
            if ele in arr1:
                res+=[ele]*hashmap[ele]
        left=[]
        for ele in arr1:
            if ele not in arr2:
                left.append(ele)
        left.sort()
        res+=left
        return res