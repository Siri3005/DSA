class Solution(object):
    def addBinary(self, a, b):
        a_int=int(a,2)
        b_int=int(b,2)
        res=a_int+b_int
        return bin(res)[2:]