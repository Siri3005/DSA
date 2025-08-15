class Solution(object):
    def intersection(self, nums1, nums2):
        n=len(nums1)
        m=len(nums2)
        arr1,arr2=[],[]
        if n<m:
            arr1[:]=nums1
            arr2[:]=nums2
        else:
            arr1[:]=nums2
            arr2[:]=nums1
        res=[]
        for num in arr1:
            if num in arr2:
                res.append(num)
        return list(set(res))
