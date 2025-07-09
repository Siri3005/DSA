class Solution(object):
    def isValid(self, s):
        dicti={'}':'{',']':'[',')':'('}
        stack=[]
        for c in s:
            if c in dicti:
                if stack and stack[-1]==dicti[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        if stack:
            return False
        else:
            return True