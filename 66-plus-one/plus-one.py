class Solution(object):
    def plusOne(self, digits):
        num=''
        for digit in digits:
            num+=str(digit)
        res_num=int(num)+1
        res=[]
        for num in str(res_num):
            res.append(int(num))
        return res

