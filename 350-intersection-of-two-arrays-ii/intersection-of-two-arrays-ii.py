class Solution(object):
    def intersect(self, nums1, nums2):
        n=len(nums1)
        m=len(nums2)
        arr1,arr2=[],[]
        hashmap1=defaultdict(int)
        hashmap2=defaultdict(int)
        for num in nums1:
            hashmap1[num]+=1
        for num in nums2:
            hashmap2[num]+=1
        if n<m:
            arr1[:]=nums1
            arr2[:]=nums2
        else:
            arr1[:]=nums2
            arr2[:]=nums1
        res=[]
        for num in arr1:
            if num in arr2 and num not in res:
                count=min(hashmap1[num],hashmap2[num])
                for i in range(count):
                    res.append(num)
        return res

        