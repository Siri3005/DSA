class Solution(object):
    def merge(self, nums1, m, nums2, n):
        i=0
        j=0
        res=[]
        while i<m and j<n:
            if nums1[i]<=nums2[j]:
                res.append(nums1[i])
                i+=1
            else:
                res.append(nums2[j])
                j+=1
        if i<m:
            res.extend(nums1[i:m])
        if j<n:
            res.extend(nums2[j:n])
        nums1[:]=res