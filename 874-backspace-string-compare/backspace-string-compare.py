class Solution(object):
    def backspaceCompare(self, s, t):
        stack1=[]
        for ch in s:
            if ch=='#':
                if stack1:
                    stack1.pop()
            else:
                stack1.append(ch)
        stack2=[]
        for ch in t:
            if ch=='#':
                if stack2:
                    stack2.pop()
            else:
                stack2.append(ch)
        if ''.join(stack1)==''.join(stack2):
            return True
        return False
        