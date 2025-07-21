class Solution(object):
    def isBalanced(self, num):
        sum_even=0
        sum_odd=0
        for i in range(len(num)):
            if i%2==0:
                sum_even+=int(num[i])
            else:
                sum_odd+=int(num[i])
        if sum_even==sum_odd:
            return True
        else:
            return False