class Solution(object):
    def sortEvenOdd(self, nums):
        odd_arr=[]
        even_arr=[]
        for i in range(len(nums)):
            if i%2!=0:
                odd_arr.append(nums[i])
            else:
                even_arr.append(nums[i])
        odd_arr.sort(reverse=True)
        even_arr.sort()
        idx1,idx2=0,0
        res=[]
        while idx1<len(odd_arr) and idx2<len(even_arr):
            res.append(even_arr[idx2])
            res.append(odd_arr[idx1])
            idx1+=1
            idx2+=1
        while idx1<len(odd_arr):
            res.append(odd_arr[idx1:])
            idx1+=1
        while idx2<len(even_arr):
            res.append(even_arr[idx2])
            idx2+=1
        return res