class Solution(object):
    def distributeCandies(self, candyType):
        n=len(candyType)
        can_eat=n//2
        cand_set=set(candyType)
        count=0
        for i in range(len(cand_set)):
            if count==can_eat:
                break
            count+=1
        return count