class Solution(object):
    def repeatedStringMatch(self, a, b):
        n=1
        repeated=a
        while len(repeated)<len(b):
            repeated+=a
            n+=1
        if b in repeated:
            return n
        repeated+=a
        if b in repeated:
            return n+1
        
        return -1

        