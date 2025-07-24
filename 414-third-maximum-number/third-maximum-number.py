class Solution(object):
    def thirdMax(self, nums):
        list1=set(nums)
        if len(list1)<3:
            return max(nums)
        list2=[]
        for num in list1:
            list2.append(num)
        list2.sort(reverse=True)
        return list2[2]
        