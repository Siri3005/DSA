class Solution(object):
    def findKthPositive(self, arr, k):
        count=0
        i=1
        res=0
        while count!=k:
            if i not in arr:
                count+=1
                res=i
            i+=1
        return res