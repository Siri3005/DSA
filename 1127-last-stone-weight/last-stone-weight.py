class Solution(object):
    def lastStoneWeight(self, stones):
        while len(stones)>1:
            stones.sort(reverse=True)
            x,y=stones[0],stones[1]
            if x==y:
                stones.pop(0)
                stones.pop(0)
            if x!=y:
                stones[1]=x-y
                stones.pop(0)
        if stones:
            return stones[0]
        else:
            return 0