class Solution(object):
    def sortPeople(self, names, heights):
        hashmap={}
        for i in range(len(names)):
            hashmap[heights[i]]=names[i]
        heights.sort(reverse=True)
        res=[]
        for height in heights:
            res.append(hashmap[height])
        return res
        