class Solution(object):
    def myAtoi(self, s):
        num=''
        numbers=set('0123456789')
        started=False
        sign=''
        for ch in s:
            if ch==' ' and not started:
                continue
            elif (ch=='+' or ch=='-') and not started:
                sign=ch
                started=True
            elif ch in numbers:
                num+=ch
                started=True
            else:
                break
        if num=='':
            return 0
        if sign=='-':
            res=-1*int(num)
        else:
            res=int(num)
        return max(-2**31,min(res,2**31-1))
        