class Solution(object):
    def isIsomorphic(self, s, t):
        if len(set(s))!=len(set(t)):
            return False
        hashmap={}
        visited=set()
        for i in range(len(s)):
            if s[i] in hashmap:
                if hashmap[s[i]]!=t[i]:
                    return False
            else:
                if t[i] in visited:
                    return False
                hashmap[s[i]]=t[i]
                visited.add(t[i])
        return True
        