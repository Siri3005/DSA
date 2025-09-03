class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i,j=0,0
        res=[]
        while i<m and j<n:
            if nums1[i]<nums2[j]:
                res.append(nums1[i])
                i+=1
            else:
                res.append(nums2[j])
                j+=1
        if i<m:
            while i<m:
                res.append(nums1[i])
                i+=1
        elif j<n:
            while j<n:
                res.append(nums2[j])
                j+=1
        nums1[:]=res[:]
        