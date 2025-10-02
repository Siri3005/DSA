class Solution(object):
    def generateParenthesis(self, n):
        res=[]
        def backtrack(s,ocount,ccount):
            if len(s)==2*n:
                res.append(s)
                return 
            if ocount<n:
                backtrack(s+'(',ocount+1,ccount)
            if ccount<ocount:
                backtrack(s+')',ocount,ccount+1)
        backtrack("",0,0)
        return res

        