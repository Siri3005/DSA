class Solution(object):
    def minimumSum(self, num):
        num_l=list(str(num))
        num_l.sort()
        summ=int(num_l[0]+num_l[2])+int(num_l[1]+num_l[3])
        return summ
        
        