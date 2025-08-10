class Solution(object):
    def clearDigits(self, s):
        digits=set('0123456789')
        stack=[]
        for ch in s:
            if ch in digits:
                if stack:
                    stack.pop()
            else:
                stack.append(ch)
        return ''.join(stack)
        