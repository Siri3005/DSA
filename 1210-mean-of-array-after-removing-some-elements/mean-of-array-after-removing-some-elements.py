class Solution(object):
    def trimMean(self, arr):
        arr.sort()
        n=len(arr)
        idx=int(n*0.05)
        for i in range(idx):
            arr[i]=None
        for i in range(len(arr)-1,len(arr)-(idx+1),-1):
            arr[i]=None
        summ=0
        count=0
        for i in range(len(arr)):
            if arr[i] is not None:
                summ+=arr[i]
                count+=1
        return float(summ)/count
