class Solution(object):
    def rotateString(self, s, goal):
        if s==goal:
            return True
        arr=list(s)
        goal=list(goal)
        for i in range(len(s)-1):
            ele=arr.pop()
            arr.insert(0,ele)
            if arr==goal:
                return True
        return False

        