class Solution(object):
    def maxProduct(self, n):
        n_str=sorted(list(str(n)))
        return int(n_str[-1])*int(n_str[-2])
        

        