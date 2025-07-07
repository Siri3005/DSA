class Solution(object):
    def countBits(self, n):
        result=[0]*(n+1)
        for i in range(n+1):
            result[i]=self.count_ones(i)
        return result
        
    def count_ones(self,n):
        res=0
        while n:
            res+=n%2
            n=n>>1
        return res
        