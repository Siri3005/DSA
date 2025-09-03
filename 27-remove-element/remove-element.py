class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        res=[]
        for ele in nums:
            if ele==val:
                continue
            res.append(ele)
        nums[:]=res[:]